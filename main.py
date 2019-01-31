import datetime
import random
import time
from pprint import pprint

# from pijuice import PiJuice
# from actuators.collectorpositioner import CollectorPositioner
from nextion.NexPlotView import NexPlotView
from nextion.NextionView import NextionView
from nextion.TextView import TextView
from protogen import hal_pb2
import socket
import threading
# from sensors.bh1750 import BH1750
# from sensors.ina219 import INA219
# from sensors.ds18b20 import DS18B20
# from sensors.BMP280 import BMP280
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32
# from actuators.ssd1306 import SSD1306
# from actuators.power_source_selector import PowerSourceSelector
import serial

# HOST = '127.0.0.1' # only for localhost
HOST = '0.0.0.0' # on all interface
PORT = 9005

# pwr_selector = PowerSourceSelector(ext_en_pin=17, solar_en_pin=27)
#
# display = SSD1306()
# env_sensor = BMP280(address=0x76)
# temp_sensor = DS18B20()
# light_sensor = BH1750(address=0x23)
# battery_source = PiJuice(bus=1, address=0x14)
# external_source = INA219(address=0x40)
# collector_source = INA219(address=0x41)
# collector_positioner = CollectorPositioner(pca9865_address=0x60, tilt_servo_ch=0)
run_display_task = True

def display_handler_task():
    anim_index = 0
    with serial.Serial('/dev/ttyUSB0', timeout=1) as dsp:
        # initialize display with several commands
        display = NextionView(conn=dsp)
        display.send_command('')
        display.send_command('bkcmd=1')
        display.send_command('page 0')
        current_page = 0
        time_view = TextView(conn=dsp, name="time")
        tilt_view = TextView(conn=dsp, name="tilt")
        rotation_view = TextView(conn=dsp, name="rotation")
        temp_view = TextView(conn=dsp, name="temp")
        humidity_view = TextView(conn=dsp, name="humidity")
        pressure_view = TextView(conn=dsp, name="pressure")
        lum_view = TextView(conn=dsp, name="lum")
        ext_voltage_plot_view = NexPlotView(conn=dsp, prefix="ext_v", comp_id=1, channel=0, max_value=10, min_value=0, format="%0.1fV")
        ext_current_plot_view = NexPlotView(conn=dsp, prefix="ext_i", comp_id=1, channel=1, max_value=1.5, min_value=0, format="%0.1fA")

        for i in range(0, 200):
            ext_voltage_plot_view.push(random.random()*2+7)
            ext_current_plot_view.push(random.random()+0.3)

        # send_data_to_display(conn=dsp, command='ext_v_top.txt="1.2V"')
        while run_display_task:
            # send_data_to_display(conn=dsp, command='ext_anim.pic='+str(14+anim_index))
            # send_data_to_display(conn=dsp, command='anim.pic='+str(10+anim_index))
            # anim_index = (anim_index+1)%3
            time_view.set_text(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
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
    pass


def main():
    global run_display_task
    threading.Thread(target=display_handler_task).start()
    # display.clear()
    # pwr_selector.select_external_source()
    # if collector_positioner is not None:
    #     collector_positioner.set_tilt_angle(0)
    #     collector_positioner.set_rotation_angle(0)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
        sck.bind((HOST, PORT))
        # display.show_connection_details(PORT)
        # display.show_message_box()
        # display.change_connected_status(False)
        print("Port:", PORT)
        print("Waiting for connection...")
        # the maximum number of queued connections: 1
        sck.listen(1)

        # if connection is interrupted, then we listen again
        try:
            while True:
                # display.change_connected_status(False)
                conn = None
                try:
                    conn, address = sck.accept()
                    # display.change_connected_status(True)
                    print("Accepted connection from:", address)
                    while True:
                        request_raw = conn.recv(200)
                        if not request_raw:
                            break

                        try:
                            n = 0
                            while n < len(request_raw):
                                msg_len, new_pos = _DecodeVarint32(request_raw, n)
                                n = new_pos
                                request_raw = request_raw[n:n+msg_len]
                                n += msg_len
                                request = hal_pb2.Request()
                                request.ParseFromString(request_raw)
                                print("Request:")
                                pprint(request)
                                response = process_request(request)
                                print("Response:")
                                pprint(response)
                                size = response.ByteSize()
                                conn.send(_VarintBytes(size))
                                conn.sendall(response.SerializeToString())
                        except:
                            print("Error during decoding message")
                            conn.close()
                            conn = None

                # keyboard interrupt must be passed to able to finish listening
                except KeyboardInterrupt:
                    raise KeyboardInterrupt

                except:
                    print("Error during establishing connection")
                    pass

                finally:
                    if conn is not None:
                        conn.close()

        except KeyboardInterrupt:
            print("Finishing listening on port ", PORT)
            pass
        finally:
            sck.close()

    run_display_task = False
    # display.clear()
    # pwr_selector.select_battery_source()
    # if collector_positioner is not None:
    #     collector_positioner.finish()
    pass


def process_request(request: hal_pb2.Request):
    response = hal_pb2.Response()

    # first set response to OK and later we can set errors with OR gate
    response.status = hal_pb2.Response.OK
    response.illuminance.value = 386.1323
    response.illuminance.unit  = hal_pb2.Illuminance.LUX
    response.status = 128

    return response

    # process data requests
    # if request.data != hal_pb2.Request.NO_THANKS:
    #
    #     # read temperature data from sensor when all data or that specific data requested
    #     if (request.data & hal_pb2.Request.INTERNAL_TEMPERATURE) > 0:
    #         success, temp = env_sensor.get_temperature()
    #         if success:
    #             response.temperature.value = temp
    #             response.temperature.unit  = hal_pb2.Temperature.CELSIUS
    #         else:
    #             response.status |= hal_pb2.Response.INT_TEMPERATURE_ERROR
    #
    #     # read humidity data from sensor when all data or that specific data requested
    #     if (request.data & hal_pb2.Request.INTERNAL_HUMIDITY) > 0:
    #         response.status |= hal_pb2.Response.HUMIDITIY_ERROR
    #
    #     # read pressure data from sensor when all data or that specific data requested
    #     if (request.data & hal_pb2.Request.INTERNAL_PRESSURE) > 0:
    #         success, pressure = env_sensor.get_pressure()
    #         if success:
    #             response.pressure.value = pressure
    #             response.pressure.unit  = hal_pb2.Pressure.HECTOPASCAL
    #         else:
    #             response.status |= hal_pb2.Response.PRESSURE_ERROR
    #
    #     # read illuminance data from sensor when all data or that specific data requested
    #     if (request.data & hal_pb2.Request.INTERNAL_ILLUMINANCE) > 0:
    #         success, lux = light_sensor.read_intensity()
    #         if success:
    #             response.illuminance.value = lux
    #             response.illuminance.unit  = hal_pb2.Illuminance.LUX
    #         else:
    #             response.status |= hal_pb2.Response.ILLUMINANCE_ERROR
    #
    #     # read ext. temperature data from sensor when all data or that specific data requested
    #     if (request.data & hal_pb2.Request.EXTERNAL_TEMPERATURE) > 0:
    #         try:
    #             success, temp = temp_sensor.temperature()
    #             if success:
    #                 response.externalTemperature.value = temp
    #                 response.externalTemperature.unit  = hal_pb2.Temperature.CELSIUS
    #             else:
    #                 response.status |= hal_pb2.Response.EXT_TEMPERATURE_ERROR
    #         except:
    #             response.status |= hal_pb2.Response.EXT_TEMPERATURE_ERROR
    #
    #     # read collector tilt data from sensor when all data or that specific data requested
    #     if (request.data & hal_pb2.Request.COLLECTOR_TILT) > 0:
    #         success, angle = collector_positioner.get_tilt_angle()
    #         if success:
    #             response.collectorTilt.value = angle
    #             response.collectorTilt.unit = hal_pb2.Angle.DEGREE
    #         else:
    #             response.status |= hal_pb2.Response.COLLECTOR_TILT_ERROR
    #
    #     # read collector rotation data from sensor when all data or that specific data requested
    #     if (request.data & hal_pb2.Request.COLLECTOR_ROTATION) > 0:
    #         success, angle = collector_positioner.get_rotation_angle()
    #         if success:
    #             response.collectorRotation.value = angle
    #             response.collectorRotation.unit = hal_pb2.Angle.DEGREE
    #         else:
    #             response.status |= hal_pb2.Response.COLLECTOR_ROTATION_ERROR
    #
    #     # read power source state from selector when all data or that specific data requested
    #     if (request.data & hal_pb2.Request.POWER_SOURCE) > 0:
    #         response.powerSource = pwr_selector.get_power_source()
    #
    #     # read battery voltage data from sensor when all data or that specific data requested
    #     if (request.data & hal_pb2.Request.BATTERY_VOLTAGE) > 0:
    #         state = battery_source.status.GetBatteryVoltage()
    #         if state['error'] == 'NO_ERROR':
    #             response.batteryDetails.voltage.value = state['data']
    #             response.batteryDetails.voltage.unit = hal_pb2.Voltage.MILLIVOLT
    #         else:
    #             response.status |= hal_pb2.Response.BATTERY_ERROR
    #
    #     if (request.data & hal_pb2.Request.BATTERY_CURRENT) > 0:
    #         state = battery_source.status.GetBatteryCurrent()
    #         if state['error'] == 'NO_ERROR':
    #             response.batteryDetails.current.value = state['data']
    #             response.batteryDetails.current.unit = hal_pb2.Current.MILLIAMPER
    #         else:
    #             response.status |= hal_pb2.Response.BATTERY_ERROR
    #
    #     if (request.data & hal_pb2.Request.BATTERY_STATE) > 0:
    #         state = battery_source.status.GetChargeLevel()
    #         if state['error'] == 'NO_ERROR':
    #             response.batteryDetails.state = str(state['data'])
    #         else:
    #             response.status |= hal_pb2.Response.BATTERY_ERROR
    #
    #     # read external power source data from sensor when all data or that specific data requested
    #     if (request.data & hal_pb2.Request.EXTERNAL_PS_VOLTAGE) > 0:
    #         try:
    #             success, voltage = external_source.bus_voltage()
    #             if success:
    #                 response.externalPSDetails.voltage.value = voltage
    #                 response.externalPSDetails.voltage.unit = hal_pb2.Voltage.MILLIVOLT
    #             else:
    #                 response.status |= hal_pb2.Response.EXTERNAL_ERROR
    #         except:
    #             response.status |= hal_pb2.Response.EXTERNAL_ERROR
    #
    #     if (request.data & hal_pb2.Request.EXTERNAL_PS_CURRENT) > 0:
    #         try:
    #             success, current = external_source.current()
    #             if success:
    #                 response.externalPSDetails.current.value = current
    #                 response.externalPSDetails.current.unit = hal_pb2.Voltage.MILLIAMPER
    #             else:
    #                 response.status |= hal_pb2.Response.EXTERNAL_ERROR
    #         except:
    #             response.status |= hal_pb2.Response.EXTERNAL_ERROR
    #
    #     if (request.data & hal_pb2.Request.EXTERNAL_PS_STATE) > 0:
    #         try:
    #             success, voltage = external_source.bus_voltage()
    #             if success:
    #                 response.externalPSDetails.state = get_power_source_state(voltage)
    #             else:
    #                 response.status |= hal_pb2.Response.EXTERNAL_ERROR
    #         except:
    #             response.status |= hal_pb2.Response.EXTERNAL_ERROR
    #
    #     # read collector power source data from sensor when all data or that specific data requested
    #     if (request.data & hal_pb2.Request.COLLECTOR_PS_VOLTAGE) > 0:
    #         try:
    #             success, voltage = collector_source.bus_voltage()
    #             if success:
    #                 response.collectorPSDetails.voltage.value = voltage
    #                 response.collectorPSDetails.voltage.unit = hal_pb2.Voltage.MILLIVOLT
    #             else:
    #                 response.status |= hal_pb2.Response.COLLECTOR_ERROR
    #         except:
    #             response.status |= hal_pb2.Response.COLLECTOR_ERROR
    #
    #     if (request.data & hal_pb2.Request.COLLECTOR_PS_CURRENT) > 0:
    #         try:
    #             success, current = collector_source.current()
    #             if success:
    #                 response.collectorPSDetails.current.value = current
    #                 response.collectorPSDetails.current.unit = hal_pb2.Voltage.MILLIAMPER
    #             else:
    #                 response.status |= hal_pb2.Response.COLLECTOR_ERROR
    #         except:
    #             response.status |= hal_pb2.Response.COLLECTOR_ERROR
    #
    #     if (request.data & hal_pb2.Request.COLLECTOR_PS_STATE) > 0:
    #         try:
    #             success, voltage = collector_source.bus_voltage()
    #             if success:
    #                 response.collectorPSDetails.state = get_power_source_state(voltage)
    #             else:
    #                 response.status |= hal_pb2.Response.COLLECTOR_ERROR
    #         except:
    #             response.status |= hal_pb2.Response.COLLECTOR_ERROR
    #
    # # process control requests
    # if request.control != hal_pb2.Request.NOTHING:
    #     if (request.control & hal_pb2.Request.SET_POWER_SOURCE) > 0:
    #         if request.source == hal_pb2.EXTERNAL:
    #             pwr_selector.select_external_source()
    #         elif request.source == hal_pb2.BATTERY:
    #             pwr_selector.select_battery_source()
    #         elif request.source == hal_pb2.COLLECTOR:
    #             pwr_selector.select_collector_source()
    #
    #     if (request.control & hal_pb2.Request.SET_COLLECTOR_TILT_ANGLE) > 0:
    #         try:
    #             success, angle = collector_positioner.set_tilt_angle(request.tilt_angle.value)
    #             if success:
    #                 response.collectorTilt.value = angle
    #                 response.collectorTilt.unit = hal_pb2.Angle.DEGREE
    #             else:
    #                 response.status |= hal_pb2.Response.COLLECTOR_TILT_ERROR
    #         except:
    #             response.status |= hal_pb2.Response.COLLECTOR_TILT_ERROR
    #
    #     if (request.control & hal_pb2.Request.SET_COLLECTOR_ROTATION_ANGLE) > 0:
    #         try:
    #             success, angle = collector_positioner.set_rotation_angle(request.rotation_angle.value)
    #             if success:
    #                 response.collectorRotation.value = angle
    #                 response.collectorRotation.unit = hal_pb2.Angle.DEGREE
    #             else:
    #                 response.status |= hal_pb2.Response.COLLECTOR_ROTATION_ERROR
    #         except:
    #             response.status |= hal_pb2.Response.COLLECTOR_ROTATION_ERROR
    #
    #     if (request.control & hal_pb2.Request.SHOW_MESSAGE) > 0:
    #         if request.message is not None and len(request.message) > 0:
    #             success = display.show_message(request.message)
    #             if not success:
    #                 response.status |= hal_pb2.Response.SHOW_MESSAGE_ERROR
    #         else:
    #             response.status |= hal_pb2.Response.SHOW_MESSAGE_ERROR
    #
    # return response


def get_power_source_state(voltage):
    states = [[6000, 'excellent'], [5000, 'good'], [4000, 'bad']]
    for state in states:
        if voltage > state[0]:
            return state[1]

    return 'insufficient'


if __name__ == '__main__':
    main()
