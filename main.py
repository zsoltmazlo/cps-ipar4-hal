import time
#from pijuice import PiJuice
from protogen import hal_pb2
import socket
from sensors.bh1750 import BH1750
from sensors.ina219 import INA219
from sensors.ds18b20 import DS18B20
from sensors.BMP280 import BMP280


from actuators.ssd1306 import SSD1306
from actuators.power_source_selector import PowerSourceSelector

# HOST = '127.0.0.1' # only for localhost
HOST = '0.0.0.0' # on all interface
PORT = 9014

external_source = INA219(0x40)
light_sensor = BH1750()
display = SSD1306()
pwr_selector = PowerSourceSelector(ext_en_pin=17, solar_en_pin=27)
env_sensor = BMP280(0x76)
temp_sensor = DS18B20()


def main():
    display.clear()
    pwr_selector.select_external_source()

    req = hal_pb2.Request()
    req.data = hal_pb2.Request.INTERNAL_TEMPERATURE
    print(req.SerializeToString())

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
        sck.bind((HOST, PORT))
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
                        request_raw = conn.recv(200)
                        if not request_raw:
                            break

                        try:
                            request.ParseFromString(request_raw)
                            response = process_request(request)
                            conn.sendall(response.SerializeToString())
                        except:
                            print("Error during decoding message")


                # keyboard interrupt must be passed to able to finish listening
                except KeyboardInterrupt:
                    raise KeyboardInterrupt

                except:
                    print("Error during establishing connection")
                finally:
                    conn.close()

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

    # first set response to OK and later we can set errors with OR gate
    response.status = hal_pb2.Response.OK

    if request.data != hal_pb2.Request.NO_THANKS:

        # read temperature data from sensor when all data or that specific data requested
        if request.data == hal_pb2.Request.INTERNAL_TEMPERATURE \
        or request.data == hal_pb2.Request.ALL:
            success, temp = env_sensor.get_temperature()
            if success:
                response.temperature.value = temp
                response.temperature.unit  = hal_pb2.Temperature.CELSIUS
            else:
                response.status |= hal_pb2.Response.INT_TEMPERATURE_ERROR

        # read humidity data from sensor when all data or that specific data requested
        if request.data == hal_pb2.Request.INTERNAL_HUMIDITY \
        or request.data == hal_pb2.Request.ALL:
            response.status |= hal_pb2.Response.HUMIDITIY_ERROR

        # read pressure data from sensor when all data or that specific data requested
        if request.data == hal_pb2.Request.INTERNAL_PRESSURE \
        or request.data == hal_pb2.Request.ALL:
            success, pressure = env_sensor.get_pressure()
            if success:
                response.pressure.value = pressure
                response.pressure.unit  = hal_pb2.Pressure.HECTOPASCAL
            else:
                response.status |= hal_pb2.Response.PRESSURE_ERROR

        # read illuminance data from sensor when all data or that specific data requested
        if request.data == hal_pb2.Request.INTERNAL_ILLUMINANCE \
        or request.data == hal_pb2.Request.ALL:
            success, lux = light_sensor.read_intensity()
            if success:
                response.illuminance.value = lux
                response.illuminance.unit  = hal_pb2.Illuminance.LUX
            else:
                response.status |= hal_pb2.Response.ILLUMINANCE_ERROR

        # read ext. temperature data from sensor when all data or that specific data requested
        if request.data == hal_pb2.Request.EXTERNAL_TEMPERATURE \
        or request.data == hal_pb2.Request.ALL:
            success, temp = temp_sensor.temperature()
            if success:
                response.externalTemperature.value = temp
                response.externalTemperature.unit  = hal_pb2.Temperature.CELSIUS
            else:
                response.status |= hal_pb2.Response.EXT_TEMPERATURE_ERROR

        # read illuminance data from sensor when all data or that specific data requested
        if request.data == hal_pb2.Request.COLLECTOR_TILT \
        or request.data == hal_pb2.Request.ALL:
            # TODO return with collector tilt angle
            response.status |= hal_pb2.Response.COLLECTOR_TILT_ERROR

        # read power source state from selector when all data or that specific data requested
        if request.data == hal_pb2.Request.POWER_SOURCE \
        or request.data == hal_pb2.Request.ALL:
            response.powerSource = pwr_selector.get_power_source()

        # read illuminance data from sensor when all data or that specific data requested
        if request.data == hal_pb2.Request.BATTERY_VOLTAGE \
        or request.data == hal_pb2.Request.BATTERY_CURRENT \
        or request.data == hal_pb2.Request.BATTERY_STATE \
        or request.data == hal_pb2.Request.ALL:
            # TODO return with battery
            response.status |= hal_pb2.Response.BATTERY_ERROR

        # read illuminance data from sensor when all data or that specific data requested
        if request.data == hal_pb2.Request.EXTERNAL_PS_VOLTAGE \
        or request.data == hal_pb2.Request.EXTERNAL_PS_CURRENT \
        or request.data == hal_pb2.Request.EXTERNAL_PS_STATE \
        or request.data == hal_pb2.Request.ALL:
            # TODO return with external
            response.status |= hal_pb2.Response.EXTERNAL_ERROR

        # read illuminance data from sensor when all data or that specific data requested
        if request.data == hal_pb2.Request.COLLECTOR_PS_VOLTAGE \
        or request.data == hal_pb2.Request.COLLECTOR_PS_CURRENT \
        or request.data == hal_pb2.Request.COLLECTOR_PS_STATE \
        or request.data == hal_pb2.Request.ALL:
            # TODO return with collector
            response.status |= hal_pb2.Response.COLLECTOR_ERROR
    return response


if __name__ == '__main__':
    main()
