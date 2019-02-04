# from pijuice import PiJuice
import threading
from task_manager import TaskManager

from actuators.collectorpositioner import CollectorPositioner
from actuators.power_source_selector import PowerSourceSelector
from actuators.ssd1306 import SSD1306

from sensors.bh1750 import BH1750
# from sensors.ina219 import INA219
# from sensors.ds18b20 import DS18B20
# from sensors.BMP280 import BMP280

HOST = '0.0.0.0' # on all interface
# HOST = '127.0.0.1' # only for localhost
PORT = 9004

# actuators
display = SSD1306()
pwr_selector = PowerSourceSelector(ext_en_pin=17, solar_en_pin=27)
collector_positioner = CollectorPositioner(pca9865_address=0x60, tilt_servo_ch=0, rotation_servo_ch=1)

# sensors
light_sensor = BH1750(address=0x23)
# env_sensor = BMP280(address=0x76)
# temp_sensor = DS18B20()
# battery_source = PiJuice(bus=1, address=0x14)
# external_source = INA219(address=0x40)
# collector_source = INA219(address=0x41)


sensor_request_lock = threading.Lock()
task_manager = TaskManager()
