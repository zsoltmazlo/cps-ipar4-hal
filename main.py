import time
#from pijuice import PiJuice
from pprint import pprint
from protogen import hal_pb2
import socket
import fcntl
import struct
from sensors.bh1750 import BH1750
from threading import Thread, Timer
from sensors.ina219 import INA219
from actuators.ssd1306 import SSD1306
from actuators.power_source_selector import PowerSourceSelector
from sensors.BMP085 import BMP085
from sensors.ds18b20 import DS18B20

PORT = 9001
update_sensors = True
values_left = 20

external_source = INA219(0x40)
light_sensor = BH1750()
display = SSD1306()
pwr_selector = PowerSourceSelector(ext_en_pin=17, solar_en_pin=27)
env_sensor = BMP085()
temp_sensor = DS18B20()


def main():
    display.clear()
    pwr_selector.select_external_source()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
        sck.bind(('127.0.0.1', PORT))
        display.show_connection_details(PORT)
        display.change_connected_status(False)
        print("Port:", PORT)
        print("Waiting for connection...")
        # the maximum number of queued connections: 1
        sck.listen(1)

        # if connection is interrupted, then we listen again
        try:
            while True:
                display.change_connected_status(False)
                try:
                    conn, address = sck.accept()
                    request = hal_pb2.Request()
                    display.change_connected_status(True)
                    print("Accepted connection from:", address)
                    while True:
                        request_raw = conn.recv(20)
                        if not request_raw:
                            break

                        request.ParseFromString(request_raw)
                        print("Request: ", request)
                        temp = hal_pb2.Temperature()
                        temp.value = 12.3
                        temp.unit = hal_pb2.Temperature.FARENHEIT
                        conn.sendall(temp.SerializeToString())
                    conn.close()

                # keyboard interrupt must be passed to able to finish listening
                except KeyboardInterrupt:
                    raise KeyboardInterrupt

                except:
                    print("Error during decoding message")
                    pass

        except KeyboardInterrupt:
            print("Finishing listening on port ", PORT)
            pass

    display.clear()
    pwr_selector.select_battery_source()
    # thread.join()
    # cap = PiJuice(1, 0x14)
    # print("IO current:"),
    # print(cap.status.GetIoCurrent())  # Read PiJuice status.
    #
    # print("\nStatus: ")
    # pprint(cap.status.GetStatus())  # Read PiJuice status.
    # print("\nCharge level:")
    # pprint(cap.status.GetChargeLevel())  # Read PiJuice status.
    # print("\nFault status:")
    # pprint(cap.status.GetFaultStatus())  # Read PiJuice status.
    # print("\nBattery temperature:")
    # pprint(cap.status.GetBatteryTemperature())  # Read PiJuice status.
    # print("\nBattery voltage:")
    # pprint(cap.status.GetBatteryVoltage())  # Read PiJuice status.
    # print("\nBattery current:")
    # pprint(cap.status.GetBatteryCurrent())  # Read PiJuice status.
    # print("\nIO voltage:")
    # pprint(cap.status.GetIoVoltage())  # Read PiJuice status.
    #
    # print("\nIO digital input:")
    # pprint(cap.status.GetIoDigitalInput(1))  # Read PiJuice status.
    pass


def process_request(request: hal_pb2.Request):
    response = hal_pb2.Response()
    response.status = hal_pb2.Response.Status.OK

    if request.data is not hal_pb2.Request.Data.NO_THANKS:
        if request.data is hal_pb2.Request.Data.INTERNAL_TEMPERATURE:
            # TODO internal temperature
            response.status |= hal_pb2.Response.Status.INT_TEMPERATURE_ERROR

        elif request.data is hal_pb2.Request.Data.INTERNAL_HUMIDITY:
            # TODO internal humidity
            response.status |= hal_pb2.Response.Status.HUMIDITIY_ERROR


        elif request.data is hal_pb2.Request.Data.INTERNAL_PRESSURE:
            try:
                pressure = env_sensor.read_pressure()
                response.pressure = hal_pb2.Pressure()
                response.pressure.value = pressure
                response.pressure.unit = hal_pb2.Pressure.Unit.PASCAL
            except:
                response.status |= hal_pb2.Response.Status.PRESSURE_ERROR

        elif request.data is hal_pb2.Request.Data.INTERNAL_ILLUMINANCE:
            try:
                illuminance = light_sensor.read_intensity()
                if illuminance[0]:
                    response.illuminance = hal_pb2.Illuminance()
                    response.illuminance.value = illuminance[1]
                    response.illuminance.unit = hal_pb2.Illuminance.Unit.LUX
                else:
                    raise RuntimeError
            except:
                response.status |= hal_pb2.Response.Status.ILLUMINANCE_ERROR

        elif request.data is hal_pb2.Request.Data.EXTERNAL_TEMPERATURE:
            try:
                temperature = light_sensor.read_intensity()
                if temperature[0]:
                    response.externalTemperature = hal_pb2.Temperature()
                    response.externalTemperature.value = temperature[1]
                    response.externalTemperature.unit = hal_pb2.Temperature.Unit.CELSIUS
                else:
                    raise RuntimeError
            except:
                response.status |= hal_pb2.Response.Status.EXT_TEMPERATURE_ERROR

        elif request.data is hal_pb2.Request.Data.COLLECTOR_TILT:
            # TODO collector tilt
            response.status |= hal_pb2.Response.Status.COLLECTOR_TILT_ERROR

        elif request.data is hal_pb2.Request.Data.POWER_SOURCE:
            response.powerSource = pwr_selector.get_power_source()

        elif request.data is hal_pb2.Request.Data.BATTERY_VOLTAGE:
            response.status |= hal_pb2.Response.Status.BATTERY_ERROR

        elif request.data is hal_pb2.Request.Data.BATTERY_CURRENT:
            response.status |= hal_pb2.Response.Status.BATTERY_ERROR

        elif request.data is hal_pb2.Request.Data.BATTERY_STATE:
            response.status |= hal_pb2.Response.Status.BATTERY_ERROR

        elif request.data is hal_pb2.Request.Data.EXTERNAL_PS_VOLTAGE:
            response.status |= hal_pb2.Response.Status.EXTERNAL_ERROR

        elif request.data is hal_pb2.Request.Data.EXTERNAL_PS_CURRENT:
            response.status |= hal_pb2.Response.Status.EXTERNAL_ERROR

        elif request.data is hal_pb2.Request.Data.EXTERNAL_PS_STATE:
            response.status |= hal_pb2.Response.Status.EXTERNAL_ERROR

        elif request.data is hal_pb2.Request.Data.COLLECTOR_PS_VOLTAGE:
            response.status |= hal_pb2.Response.Status.COLLECTOR_ERROR

        elif request.data is hal_pb2.Request.Data.COLLECTOR_PS_CURRENT:
            response.status |= hal_pb2.Response.Status.COLLECTOR_ERROR

        elif request.data is hal_pb2.Request.Data.COLLECTOR_PS_STATE:
            response.status |= hal_pb2.Response.Status.COLLECTOR_ERROR
    pass


if __name__ == '__main__':
    main()
