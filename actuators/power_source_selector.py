from gpiozero import LED
# from protogen.hal_pb2 import PowerSource


class PowerSourceSelector:

    def __init__(self, ext_en_pin, solar_en_pin):
        self.ext_en = LED(ext_en_pin)
        self.solar_en = LED(solar_en_pin)
        self.ext_en.off()
        self.solar_en.off()
        self.source = None
        # self.source = PowerSource.BATTERY

    def get_power_source(self):
        return self.source

    def select_external_source(self):
        self.solar_en.off()
        self.ext_en.on()
        # self.source = PowerSource.EXTERNAL

    def select_collector_source(self):
        self.ext_en.off()
        self.solar_en.on()
        # self.source = PowerSource.COLLECTOR

    def select_battery_source(self):
        self.ext_en.off()
        self.solar_en.off()
        # self.source = PowerSource.BATTERY

