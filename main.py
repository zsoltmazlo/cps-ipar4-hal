from pijuice import PiJuice
from actuators.collectorpositioner import CollectorPositioner
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
PORT = 9002

display = SSD1306()
env_sensor = BMP280(address=0x76)
temp_sensor = DS18B20()
light_sensor = BH1750(address=0x23)
pwr_selector = PowerSourceSelector(ext_en_pin=17, solar_en_pin=27)

battery_source = PiJuice(bus=1, address=0x14)
external_source = INA219(address=0x40)
collector_source = INA219(address=0x41)
tilt_actuator = CollectorPositioner(pca9865_address=0x60)


def main():
    display.clear()
    pwr_selector.select_external_source()
    tilt_actuator.set_angle(0)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
        sck.bind((HOST, PORT))
        display.show_connection_details(PORT)
        display.show_message_box()
        display.change_connected_status(False)
        print("Port:", PORT)
        print("Waiting for connection...")
        # the maximum number of queued connections: 1
        sck.listen(1)

        # if connection is interrupted, then we listen again
        try:
            while True:
                display.change_connected_status(False)
                conn = None
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

    display.clear()
    pwr_selector.select_battery_source()
    tilt_actuator.finish()
    pass


def process_request(request: hal_pb2.Request):
    response = hal_pb2.Response()

    # first set response to OK and later we can set errors with OR gate
    response.status = hal_pb2.Response.OK

    # process data requests
    if request.data != hal_pb2.Request.NO_THANKS:

        # read temperature data from sensor when all data or that specific data requested
        if (request.data & hal_pb2.Request.INTERNAL_TEMPERATURE) > 0:
            success, temp = env_sensor.get_temperature()
            if success:
                response.temperature.value = temp
                response.temperature.unit  = hal_pb2.Temperature.CELSIUS
            else:
                response.status |= hal_pb2.Response.INT_TEMPERATURE_ERROR

        # read humidity data from sensor when all data or that specific data requested
        if (request.data & hal_pb2.Request.INTERNAL_HUMIDITY) > 0:
            response.status |= hal_pb2.Response.HUMIDITIY_ERROR

        # read pressure data from sensor when all data or that specific data requested
        if (request.data & hal_pb2.Request.INTERNAL_PRESSURE) > 0:
            success, pressure = env_sensor.get_pressure()
            if success:
                response.pressure.value = pressure
                response.pressure.unit  = hal_pb2.Pressure.HECTOPASCAL
            else:
                response.status |= hal_pb2.Response.PRESSURE_ERROR

        # read illuminance data from sensor when all data or that specific data requested
        if (request.data & hal_pb2.Request.INTERNAL_ILLUMINANCE) > 0:
            success, lux = light_sensor.read_intensity()
            if success:
                response.illuminance.value = lux
                response.illuminance.unit  = hal_pb2.Illuminance.LUX
            else:
                response.status |= hal_pb2.Response.ILLUMINANCE_ERROR

        # read ext. temperature data from sensor when all data or that specific data requested
        if (request.data & hal_pb2.Request.EXTERNAL_TEMPERATURE) > 0:
            try:
                success, temp = temp_sensor.temperature()
                if success:
                    response.externalTemperature.value = temp
                    response.externalTemperature.unit  = hal_pb2.Temperature.CELSIUS
                else:
                    response.status |= hal_pb2.Response.EXT_TEMPERATURE_ERROR
            except:
                response.status |= hal_pb2.Response.EXT_TEMPERATURE_ERROR

        # read collector tilt data from sensor when all data or that specific data requested
        if (request.data & hal_pb2.Request.COLLECTOR_TILT) > 0:
            try:
                success, angle = tilt_actuator.get_tilt_angle()
                if success:
                    response.collectorTilt.value = angle
                    response.collectorTilt.unit = hal_pb2.Angle.DEGREE
                else:
                    request.status |= hal_pb2.Response.COLLECTOR_TILT_ERROR
            except:
                request.status |= hal_pb2.Response.COLLECTOR_TILT_ERROR

        # read collector rotation data from sensor when all data or that specific data requested
        if (request.data & hal_pb2.Request.COLLECTOR_ROTATION) > 0:
                request.status |= hal_pb2.Response.COLLECTOR_ROTATION_ERROR

        # read power source state from selector when all data or that specific data requested
        if (request.data & hal_pb2.Request.POWER_SOURCE) > 0:
            response.powerSource = pwr_selector.get_power_source()

        # read battery voltage data from sensor when all data or that specific data requested
        if (request.data & hal_pb2.Request.BATTERY_VOLTAGE) > 0:
            state = battery_source.status.GetBatteryVoltage()
            if state['error'] == 'NO_ERROR':
                response.batteryDetails.voltage.value = state['data']
                response.batteryDetails.voltage.unit = hal_pb2.Voltage.MILLIVOLT
            else:
                response.status |= hal_pb2.Response.BATTERY_ERROR

        if (request.data & hal_pb2.Request.BATTERY_CURRENT) > 0:
            state = battery_source.status.GetBatteryCurrent()
            if state['error'] == 'NO_ERROR':
                response.batteryDetails.current.value = state['data']
                response.batteryDetails.current.unit = hal_pb2.Current.MILLIAMPER
            else:
                response.status |= hal_pb2.Response.BATTERY_ERROR

        if (request.data & hal_pb2.Request.BATTERY_STATE) > 0:
            state = battery_source.status.GetChargeLevel()
            if state['error'] == 'NO_ERROR':
                response.batteryDetails.state = str(state['data'])
            else:
                response.status |= hal_pb2.Response.BATTERY_ERROR

        # read external power source data from sensor when all data or that specific data requested
        if (request.data & hal_pb2.Request.EXTERNAL_PS_VOLTAGE) > 0:
            try:
                success, voltage = external_source.bus_voltage()
                if success:
                    response.externalPSDetails.voltage.value = voltage
                    response.externalPSDetails.voltage.unit = hal_pb2.Voltage.MILLIVOLT
                else:
                    response.status |= hal_pb2.Response.EXTERNAL_ERROR
            except:
                response.status |= hal_pb2.Response.EXTERNAL_ERROR

        if (request.data & hal_pb2.Request.EXTERNAL_PS_CURRENT) > 0:
            try:
                success, current = external_source.current()
                if success:
                    response.externalPSDetails.current.value = current
                    response.externalPSDetails.current.unit = hal_pb2.Voltage.MILLIAMPER
                else:
                    response.status |= hal_pb2.Response.EXTERNAL_ERROR
            except:
                response.status |= hal_pb2.Response.EXTERNAL_ERROR

        if (request.data & hal_pb2.Request.EXTERNAL_PS_STATE) > 0:
            try:
                success, voltage = external_source.bus_voltage()
                if success:
                    response.externalPSDetails.state = get_power_source_state(voltage)
                else:
                    response.status |= hal_pb2.Response.EXTERNAL_ERROR
            except:
                response.status |= hal_pb2.Response.EXTERNAL_ERROR

        # read collector power source data from sensor when all data or that specific data requested
        if (request.data & hal_pb2.Request.COLLECTOR_PS_VOLTAGE) > 0:
            try:
                success, voltage = collector_source.bus_voltage()
                if success:
                    response.collectorPSDetails.voltage.value = voltage
                    response.collectorPSDetails.voltage.unit = hal_pb2.Voltage.MILLIVOLT
                else:
                    response.status |= hal_pb2.Response.COLLECTOR_ERROR
            except:
                response.status |= hal_pb2.Response.COLLECTOR_ERROR

        if (request.data & hal_pb2.Request.COLLECTOR_PS_CURRENT) > 0:
            try:
                success, current = collector_source.current()
                if success:
                    response.collectorPSDetails.current.value = current
                    response.collectorPSDetails.current.unit = hal_pb2.Voltage.MILLIAMPER
                else:
                    response.status |= hal_pb2.Response.COLLECTOR_ERROR
            except:
                response.status |= hal_pb2.Response.COLLECTOR_ERROR

        if (request.data & hal_pb2.Request.COLLECTOR_PS_STATE) > 0:
            try:
                success, voltage = collector_source.bus_voltage()
                if success:
                    response.collectorPSDetails.state = get_power_source_state(voltage)
                else:
                    response.status |= hal_pb2.Response.COLLECTOR_ERROR
            except:
                response.status |= hal_pb2.Response.COLLECTOR_ERROR

    # process control requests
    if request.control != hal_pb2.Request.NOTHING:
        if (request.control & hal_pb2.Request.SET_POWER_SOURCE) > 0:
            if request.source == hal_pb2.EXTERNAL:
                pwr_selector.select_external_source()
            elif request.source == hal_pb2.BATTERY:
                pwr_selector.select_battery_source()
            elif request.source == hal_pb2.COLLECTOR:
                pwr_selector.select_collector_source()

        if (request.control & hal_pb2.Request.SET_COLLECTOR_TILT_ANGLE) > 0:
            try:
                success, angle = tilt_actuator.set_tilt_angle(request.angle.value)
                if success:
                    response.collectorTilt.value = angle
                    response.collectorTilt.unit = hal_pb2.Angle.DEGREE
                else:
                    request.status |= hal_pb2.Response.COLLECTOR_TILT_ERROR
            except:
                request.status |= hal_pb2.Response.COLLECTOR_TILT_ERROR

        if (request.control & hal_pb2.Request.SET_COLLECTOR_ROTATION_ANGLE) > 0:
            request.status |= hal_pb2.Response.COLLECTOR_ROTATION_ERROR

        if (request.control & hal_pb2.Request.SHOW_MESSAGE) > 0:
            if request.message is not None and len(request.message) > 0:
                success = display.show_message(request.message)
                if not success:
                    request.status |= hal_pb2.Response.SHOW_MESSAGE_ERROR
            else:
                request.status |= hal_pb2.Response.SHOW_MESSAGE_ERROR

    return response


def get_power_source_state(voltage):
    states = [[6000, 'excellent'], [5000, 'good'], [4000, 'bad']]
    for state in states:
        if voltage > state[0]:
            return state[1]

    return 'insufficient'


if __name__ == '__main__':
    main()
