import socket
import time
from pprint import pprint

from protogen import hal_pb2


def socket_test(host, port, tilt_angle=None, rotation_angle=None, message=None, source=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
        sck.connect((host, port))
        print("Connected to socket, sending test data")

        tmp = hal_pb2.Request()
        tmp.data = hal_pb2.Request.COLLECTOR_PS_STATE*2-1

        if tilt_angle is not None:
            tmp.control |= hal_pb2.Request.SET_COLLECTOR_TILT_ANGLE
            tmp.tilt_angle.value = tilt_angle
            tmp.tilt_angle.unit = hal_pb2.Angle.DEGREE

        if rotation_angle is not None:
            tmp.control |= hal_pb2.Request.SET_COLLECTOR_ROTATION_ANGLE
            tmp.rotation_angle.value = rotation_angle
            tmp.rotation_angle.unit = hal_pb2.Angle.DEGREE

        if message is not None:
            tmp.control |= hal_pb2.Request.SHOW_MESSAGE
            tmp.message = message

        if source is not None:
            tmp.control |= hal_pb2.Request.SET_POWER_SOURCE
            tmp.source = source

        sck.sendall(tmp.SerializeToString())
        data = sck.recv(200)
        resp = hal_pb2.Response()
        resp.ParseFromString(data)
        print("Received response:")
        pprint(resp)
        time.sleep(5)
    pass


def display_debug_data(display, port=9001, light_sensor=None, external_source=None, temp_sensor=None, env_sensor=None):
    display.draw_text(0, 0, "P: ")
    display.draw_text(54, 0, "L: ")

    display.draw_text(0, 12, "C: ")
    display.draw_text(0, 24, "Vb: ")
    display.draw_text(0, 36, "Vs: ")
    display.draw_text(0, 48, "A: ")

    display.draw_text(64, 12, "T: ")
    display.draw_text(64, 36, "H: ")
    display.draw_text(64, 48, "P: ")
    display.draw_text(20, 0, str(port))

    # now = datetime.datetime.now().strftime("%H:%M:%S")
    light_level = light_sensor.read_intensity()
    current = external_source.current()
    bus_v = external_source.bus_voltage()
    v = external_source.voltage()

    display.clear(20, 24, 128 - 20, 12)
    display.draw_text(20, 24, format(bus_v, '.1f') + "mV")

    display.clear(20, 36, 63 - 20, 12)
    display.draw_text(20, 36, format(v, '.1f') + "mV")

    display.clear(20, 48, 63 - 20, 12)
    display.draw_text(20, 48, format(current, '.1f') + 'mA')

    display.clear(70, 0, 128 - 70, 12)
    display.draw_text(70, 0, format(light_level, '.2f') + "lx")

    display.clear(80, 12, 128 - 86, 12)
    display.draw_text(80, 12, format(temp_sensor.temperature()[1], '.1f') + "C")

    display.clear(80, 48, 128 - 86, 12)
    display.draw_text(80, 48, format(env_sensor.read_pressure() / 100, '.1f') + "hPa")




