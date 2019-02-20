

class Status:

    def __init__(self):
        pass

    def GetBatteryVoltage(self):
        result = dict()
        result['error'] = "NO_ERROR"
        result['data'] = 3887.32
        return result

    def GetBatteryCurrent(self):
        result = dict()
        result['error'] = "NO_ERROR"
        result['data'] = 787.44
        return result

    def GetChargeLevel(self):
        result = dict()
        result['error'] = "NO_ERROR"
        result['data'] = "MOCKED"
        return result


class PiJuice:

    status = Status()

    def __init__(self, bus, address):
        pass
