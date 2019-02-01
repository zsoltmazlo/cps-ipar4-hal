import string
import threading

import serial


class NextionView:
    lock = threading.Lock()

    def __init__(self, conn: serial.Serial):
        self.conn = conn
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def set_value(self, value):
        pass

    def update(self):
        if self.callback is not None:
            success, value = self.callback()
            if success:
                self.set_value(value)

    def send_command(self, command: string):
        cmd = bytes(command, 'utf-8')
        pos = cmd.find(0xc2)
        while pos != -1:
            cmd = cmd[0:pos]+cmd[pos+1:]
            pos = cmd.find(0xc2)

        NextionView.lock.acquire()
        self.conn.write(cmd)
        self.conn.write(b'\xFF')
        self.conn.write(b'\xFF')
        self.conn.write(b'\xFF')
        NextionView.lock.release()
