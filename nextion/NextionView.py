import string

import serial


class NextionView:

    def __init__(self, conn: serial.Serial):
        self.conn = conn

    def send_command(self, command: string):
        cmd = bytes(command, 'utf-8')
        pos = cmd.find(0xc2)
        while pos != -1:
            cmd = cmd[0:pos]+cmd[pos+1:]
            pos = cmd.find(0xc2)
        self.conn.write(cmd)
        self.conn.write(b'\xFF')
        self.conn.write(b'\xFF')
        self.conn.write(b'\xFF')
