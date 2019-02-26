import datetime
import functools
import math
import random
import string
import threading
import time

import serial

from nextion.NexPlotView import NexPlotView
from nextion.NextionView import NextionView
from nextion.SensorView import SensorView
from nextion.SpriteBasedAnimationView import SpriteBasedAnimationView
from nextion.TextView import TextView
from protogen import hal_pb2
from config import pwr_selector, collector_positioner, light_sensor, sensor_request_lock, task_manager, env_sensor, \
    external_source, panel_source, battery_source


def update_views_task(task_name: string, views:[], dt=100):
    while task_manager.is_task_running(task_name):
        for view in views:
            view.update()
        i = 100
        while i <= dt and task_manager.is_task_running(task_name):
            time.sleep(i/1000.0)
            i += 100


def read_sensor_value(fn):
    sensor_request_lock.acquire()
    s, v = fn()
    sensor_request_lock.release()
    return s, v


def display_handler_task():
    with serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=1) as dsp:
        # initialize display with several commands
        display = NextionView(conn=dsp)
        display.send_command('')
        display.send_command('bkcmd=1') # return only with success daa
        display.send_command('thdra=0') # disable touch show
        display.send_command('page 0') # goto page 0
        current_page = 0

        # pic
        # 0: background
        # 1: bat icon
        # 2: coll icon
        # 3: ext icon
        # 4-5-6: animation: battery as input
        # 7-8-9: animation: collector as input
        # 10-11-12: animation: external as input
        # 13: rail: disabled
        # 14-15-16: rail animation
        # 17: animation: disabled
        # 18: greenhouse icon
        # 19: temperature icon
        time_view = TextView(conn=dsp, name="time")
        time_view.set_callback(lambda: (True, datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))

        tilt_view = SensorView(conn=dsp, name="tilt", format="%0.0f°")
        tilt_view.set_callback(functools.partial(read_sensor_value, collector_positioner.get_tilt_angle))

        rotation_view = SensorView(conn=dsp, name="rotation", format="%0.0f°")
        rotation_view.set_callback(functools.partial(read_sensor_value, collector_positioner.get_rotation_angle))

        temp_view = SensorView(conn=dsp, name="temp", format="%0.2f°C")
        temp_view.set_callback(functools.partial(read_sensor_value, env_sensor.get_temperature))
        humidity_view = SensorView(conn=dsp, name="humidity", format="%0.2f%%")
        humidity_view.set_callback(functools.partial(read_sensor_value, env_sensor.get_humidity))
        pressure_view = SensorView(conn=dsp, name="pressure", format="%0.2fhPa")
        pressure_view.set_callback(functools.partial(read_sensor_value, env_sensor.get_pressure))

        lum_view = SensorView(conn=dsp, name="lum", format="%0.2flx")
        lum_view.set_callback(functools.partial(read_sensor_value, light_sensor.read_intensity))

        ext_voltage_plot_view = NexPlotView(conn=dsp, prefix="ext_v", comp_id=1, channel=0,
                                            max_value=10, min_value=0, format="%0.1fV", value_format="%0.2fV")
        ext_voltage_plot_view.set_callback(functools.partial(read_sensor_value, external_source.voltage))
        ext_voltage_view = SensorView(conn=dsp, name="ext_v", format="%.0fmV")
        ext_voltage_view.set_callback(functools.partial(read_sensor_value, external_source.bus_voltage))

        ext_current_plot_view = NexPlotView(conn=dsp, prefix="ext_i", comp_id=1, channel=1,
                                            max_value=1.5, min_value=0, format="%0.1fA", value_format="%0.2fA")
        ext_current_plot_view.set_callback(functools.partial(read_sensor_value, external_source.current))
        ext_current_view = SensorView(conn=dsp, name="ext_i", format="%.0fmA")
        ext_current_view.set_callback(functools.partial(read_sensor_value, external_source.current))

        bat_voltage_plot_view = NexPlotView(conn=dsp, prefix="bat_v", comp_id=6, channel=0,
                                            max_value=5, min_value=3, format="%0.1fV", value_format="%0.2fV")
        bat_voltage_plot_view.set_callback(functools.partial(read_sensor_value, battery_source.voltage))
        bat_voltage_view = SensorView(conn=dsp, name="bat_v", format="%.0fmV")
        bat_voltage_view.set_callback(functools.partial(read_sensor_value, battery_source.bus_voltage))

        bat_current_plot_view = NexPlotView(conn=dsp, prefix="bat_i", comp_id=6, channel=1,
                                            max_value=1.5, min_value=0, format="%0.1fA", value_format="%0.2fA")
        bat_current_plot_view.set_callback(functools.partial(read_sensor_value, battery_source.current))
        bat_current_view = SensorView(conn=dsp, name="bat_i", format="%.0fmA")
        bat_current_view.set_callback(functools.partial(read_sensor_value, battery_source.current))

        coll_voltage_plot_view = NexPlotView(conn=dsp, prefix="coll_v", comp_id=7, channel=0,
                                             max_value=10, min_value=0, format="%0.1fV", value_format="%0.2fV")
        coll_voltage_plot_view.set_callback(functools.partial(read_sensor_value, panel_source.voltage))
        coll_voltage_view = SensorView(conn=dsp, name="coll_v", format="%.0fmV")
        coll_voltage_view.set_callback(functools.partial(read_sensor_value, panel_source.bus_voltage))

        coll_current_plot_view = NexPlotView(conn=dsp, prefix="coll_i", comp_id=7, channel=1,
                                             max_value=1.5, min_value=0, format="%0.1fA", value_format="%0.2fA")
        coll_current_plot_view.set_callback(functools.partial(read_sensor_value, panel_source.current))
        coll_current_view = SensorView(conn=dsp, name="coll_i", format="%.0fmA")
        coll_current_view.set_callback(functools.partial(read_sensor_value, panel_source.current))

        # power source input animatiom
        ext_anim = SpriteBasedAnimationView(conn=dsp, name="ext_anim", sprite_indices=[14, 15, 16], disabled_sprite=13)
        bat_anim = SpriteBasedAnimationView(conn=dsp, name="bat_anim", sprite_indices=[14, 15, 16], disabled_sprite=13)
        coll_anim = SpriteBasedAnimationView(conn=dsp, name="coll_anim", sprite_indices=[14, 15, 16], disabled_sprite=13)
        common_anim = SpriteBasedAnimationView(conn=dsp, name="anim", sprite_indices=[4, 5, 6], disabled_sprite=17)
        bat_anim.disable()
        coll_anim.disable()
        ext_anim.disable()

        # starting a thread with 100ms sleep time to update animations and time
        threads = []
        t1 = threading.Thread(target=update_views_task,
                         args=("animation update task", [ext_anim, bat_anim, coll_anim, common_anim, time_view], 100))
        task_manager.run_task(task_name="animation update task", task=t1)
        threads.append("animation update task")

        # starting a thread with 500ms (0.5s) sleep time to update sensor data
        t2 = threading.Thread(target=update_views_task,
                         args=("quick sensor data update task",
                               [tilt_view, rotation_view,
                                ext_voltage_view, ext_current_view,
                                bat_voltage_view, bat_current_view,
                                coll_voltage_view, coll_current_view], 500))
        task_manager.run_task(task_name="quick sensor data update task", task=t2)
        threads.append("quick sensor data update task")

        # starting a thread with 200000ms (200s) sleep time to update sensor data
        t3 = threading.Thread(target=update_views_task,
                         args=("plot update task",
                               [ext_voltage_plot_view, ext_current_plot_view,
                                bat_voltage_plot_view, bat_current_plot_view,
                                coll_voltage_plot_view, coll_current_plot_view], 200000))
        task_manager.run_task(task_name="plot update task", task=t3)
        threads.append("plot update task")

        # starting a thread with 60000ms (60s) sleep time to update sensor data
        t4 = threading.Thread(target=update_views_task,
                         args=("slow sensor data update task",
                               [temp_view, pressure_view, humidity_view, lum_view], 1000))
        task_manager.run_task(task_name="slow sensor data update task", task=t4)
        threads.append("slow sensor data update task")

        prev_pwr_source = None
        display.send_command('dim=100')

        while task_manager.is_task_running("display handler"):
            sensor_request_lock.acquire()
            current_pwr_source = pwr_selector.get_power_source()
            sensor_request_lock.release()
            if prev_pwr_source is None or current_pwr_source != prev_pwr_source:
                prev_pwr_source = current_pwr_source
                if current_pwr_source == hal_pb2.EXTERNAL:
                    common_anim.set_offset(6)
                    coll_anim.disable()
                    bat_anim.disable()
                    ext_anim.enable()
                    common_anim.enable()
                elif current_pwr_source == hal_pb2.COLLECTOR:
                    common_anim.set_offset(3)
                    coll_anim.enable()
                    bat_anim.disable()
                    ext_anim.disable()
                    common_anim.enable()
                elif current_pwr_source == hal_pb2.BATTERY:
                    common_anim.set_offset(0)
                    coll_anim.disable()
                    bat_anim.enable()
                    ext_anim.disable()
                    common_anim.enable()

            time.sleep(0.1)
            display.send_command('sendme')
            recv = dsp.read_all()
            if len(recv) > 0:
                page_id = recv[1]
                if current_page != page_id and page_id != 255:
                    print("changing page to", page_id)
                    current_page = page_id
                    if page_id == 1:
                        ext_voltage_plot_view.show_values()
                        ext_current_plot_view.show_values()
                        ext_voltage_plot_view.update_min_max_label()
                        ext_current_plot_view.update_min_max_label()
                    elif page_id == 2:
                        coll_voltage_plot_view.show_values()
                        coll_current_plot_view.show_values()
                        coll_voltage_plot_view.update_min_max_label()
                        coll_current_plot_view.update_min_max_label()
                    elif page_id == 3:
                        bat_voltage_plot_view.show_values()
                        bat_current_plot_view.show_values()
                        bat_voltage_plot_view.update_min_max_label()
                        bat_current_plot_view.update_min_max_label()

        print("Closing display")

        try:
            for th in threads:
                task_manager.finish_task(th)
        except:
            pass

        display.send_command('dim=0')
        display.send_command('page 0')
        coll_anim.disable()
        bat_anim.disable()
        ext_anim.disable()
        common_anim.disable()

        # serial connection ends here
    pass
