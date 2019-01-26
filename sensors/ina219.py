import board
import busio
import adafruit_ina219


class INA219:

    def __init__(self, address=0x40):
        i2c = busio.I2C(board.SCL, board.SDA)
        try:
            self.sensor = adafruit_ina219.INA219(i2c, address)
        except:
            self.sensor = None

    def voltage(self):
        if self.sensor is None:
            return False, 0

        try:
            return True, self.sensor.shunt_voltage * 1000
        except OSError:
            print("Error during reading shunt voltage from INA219")
        return False, 0

    def bus_voltage(self):
        if self.sensor is None:
            return False, 0

        try:
            return True, self.sensor.bus_voltage * 1000
        except OSError:
            print("Error during reading bus voltage from INA219")
        return False, 0

    def current(self):
        if self.sensor is None:
            return False, 0

        try:
            return True, self.sensor.current
        except OSError:
            print("Error during reading current from INA219")
        return False, 0

