import string
import serial

from nextion.TextView import TextView


class SensorView(TextView):

    def __init__(self, conn:serial.Serial, name:string, format:string):
        TextView.__init__(self, conn=conn, name=name)
        self.format = format
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def set_value(self, value:float):
        self.set_text(self.format % (value))

    def update_value(self):
        if self.callback is not None:
            success, value = self.callback()
            if success:
                self.set_value(value)
