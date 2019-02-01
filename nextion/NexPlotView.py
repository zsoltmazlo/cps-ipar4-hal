import serial

from nextion.NextionView import NextionView
from nextion.SensorView import SensorView
from nextion.TextView import TextView


class NexPlotView(NextionView):

    def __init__(self, conn: serial.Serial, prefix, comp_id, channel, max_value, min_value, format, value_format):
        NextionView.__init__(self, conn=conn)
        self.channel = channel
        self.comp_id = comp_id
        self.prefix = prefix
        self.format = format
        self.value_view = SensorView(conn, name=self.prefix, format=value_format)
        self.max_value_view = TextView(conn, self.prefix + "_top")
        self.min_value_view = TextView(conn, self.prefix + "_bot")
        self.min_value = min_value
        self.max_value = max_value
        self.values = []
        # calculate the full range of the plot and set values
        diff = max_value - min_value
        self.max_value_view.set_text(format % (diff / 5.0 * 4.0 + self.min_value))
        self.min_value_view.set_text(format % (diff / 5.0 * 1.0 + self.min_value))

    def push(self, value):
        # map value to min-max range
        val = int((value - self.min_value) * 1.0 / (self.max_value - self.min_value) * 200.0)
        if len(self.values) < 400:
            self.values.append(val)
        else:
            self.values.pop(0)
            self.values.append(val)

    def update_value(self, value):
        self.push(value)
        self.value_view.set_value(value)

    def show_values(self):
        for val in reversed(self.values):
            self.send_command("add %d,%d,%d" % (self.comp_id, self.channel, val))

    def update_min_max_label(self):
        diff = self.max_value - self.min_value
        self.max_value_view.set_text(self.format % (diff / 5.0 * 4.0 + self.min_value))
        self.min_value_view.set_text(self.format % (diff / 5.0 * 1.0 + self.min_value))
