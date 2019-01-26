import board
import busio
import adafruit_ina219


class INA219:

    def __init__(self, address=0x40):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_ina219.INA219(i2c, address)

    def voltage(self):
        try:
            return self.sensor.shunt_voltage * 1000
        except OSError:
            print("Error during reading shunt voltage from INA219")
        return 0
        pass

    def bus_voltage(self):
        try:
            return self.sensor.bus_voltage * 1000
        except OSError:
            print("Error during reading bus voltage from INA219")
        return 0
        pass

    def current(self):
        try:
            return self.sensor.current
        except OSError:
            print("Error during reading current from INA219")
        return 0
        pass

