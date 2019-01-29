import board
import busio
from adafruit_bmp280 import Adafruit_BMP280_I2C


class BMP280:

    def __init__(self, address=0x77):
        self.bus = busio.I2C(board.SCL, board.SDA)
        try:
            self.sensor = Adafruit_BMP280_I2C(self.bus, address=address)
        except:
            print("BME280 sensor could not initiated")
            self.sensor = None

    def get_temperature(self):
        if self.sensor is None:
            return False, 0

        try:
            return True, self.sensor.temperature
        except OSError:
            return False, 0

    def get_humidity(self):
        return False, 0

    def get_pressure(self):
        if self.sensor is None:
            return False, 0

        try:
            return True, self.sensor.pressure
        except OSError:
            return False, 0
