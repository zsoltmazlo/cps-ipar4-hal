import serial
from nextion.NextionView import NextionView


class TextView(NextionView):

    def __init__(self, conn: serial.Serial, name):
        NextionView.__init__(self, conn=conn)
        self.name = name

    def set_text(self, text):
        self.send_command(self.name + ".txt=\"" + text + "\"")
