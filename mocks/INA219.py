class INA219Mock:

    def __init__(self, address=0x40):
        pass

    def voltage(self):
        return True, 9018.91

    def bus_voltage(self):
        return True, 9018.91

    def current(self):
        return True, 443.81

