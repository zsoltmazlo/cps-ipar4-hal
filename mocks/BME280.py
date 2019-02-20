class BME280:

    def __init__(self, address=0x77):
        pass

    def get_temperature(self):
        return True, 25.01

    def get_humidity(self):
        return True, 43.12

    def get_pressure(self):
        return True, 970.31
