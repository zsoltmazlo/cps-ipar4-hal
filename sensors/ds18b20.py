import time


class DS18B20:

    def __init__(self):
        self.sensor = '/sys/bus/w1/devices/28-0417710f0fff/w1_slave'

    def __temp_raw(self):
        with open(self.sensor, 'r') as f:
            lines = f.readlines()
            return lines

    def temperature(self):
        lines = self.__temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.__temp_raw()
        temp_output = lines[1].find('t=')
        if temp_output != -1:
            temp_string = lines[1].strip()[temp_output+2:]
            temp_c = float(temp_string) / 1000.0
            return True, temp_c
        return False, 0.0
