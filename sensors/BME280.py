import board
import busio
from adafruit_bme280 import Adafruit_BME280_I2C


class BME280:

    def __init__(self, address=0x76):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        try:
            self.sensor = Adafruit_BME280_I2C(i2c=self.i2c, address=address)
            self.sensor.sea_level_pressure = 1013.25
        except:
            self.sensor = None
        pass

    def get_temperature(self):
        if self.sensor is None:
            return False, 0.0

        return True, self.sensor.temperature

    def get_humidity(self):
        if self.sensor is None:
            return False, 0.0

        return True, self.sensor.humidity

    def get_pressure(self):
        if self.sensor is None:
            return False, 0.0

        return True, self.sensor.pressure

