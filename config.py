import threading
from task_manager import TaskManager

from actuators.collectorpositioner import CollectorPositioner
from actuators.power_source_selector import PowerSourceSelector
from actuators.ssd1306 import SSD1306
# from pijuice import PiJuice

from sensors.bh1750 import BH1750
from sensors.ina219 import INA219
from sensors.ds18b20 import DS18B20
from sensors.BME280 import BME280

# mocked classes, each of them returns with constant values
from mocks.PiJuice import PiJuice
# from mocks.INA219 import INA219Mock

HOST = '0.0.0.0' # on all interface
# HOST = '127.0.0.1' # only for localhost
PORT = 9007

#      0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
# 00:          -- -- -- -- -- -- -- -- -- -- -- -- --
# 10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 20: -- -- -- 23 -- -- -- -- -- -- -- -- -- -- -- --
# 30: -- -- -- -- -- -- 36 -- -- -- -- -- 3c -- -- --
# 40: 40 41 -- -- 44 45 -- -- -- -- -- -- -- -- -- --
# 50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 70: 70 -- -- -- -- -- 76 --
#
# 14: PiJuice
# 23: BH1750
# 36: MAX17043
# 3c: SSD1306
# 40: PCA9685
# 41: INA219 (solar)
# 44: INA219 (external)
# 44: INA219 (battery)
# 70: PCA9685??
# 76: BME280
#
# https://datasheets.maximintegrated.com/en/ds/MAX17043-MAX17044.pdf
# The  7-bit  slave  address  is  fixed  to  6Ch (write)/6Dh (read)

# actuators
display = SSD1306()
pwr_selector = PowerSourceSelector(ext_en_pin=9, solar_en_pin=10)
collector_positioner = CollectorPositioner(pca9865_address=0x40, en_pin=26, tilt_servo_ch=0, rotation_servo_ch=1)

# sensors
light_sensor = BH1750(address=0x23)
env_sensor = BME280(address=0x76)
temp_sensor = DS18B20()
# battery_source = PiJuice(bus=1, address=0x14)
battery_source = INA219(address=0x45)
external_source = INA219(address=0x44)
panel_source = INA219(address=0x41)


sensor_request_lock = threading.Lock()
task_manager = TaskManager()
