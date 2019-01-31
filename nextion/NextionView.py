import serial


class NextionView:

    def __init__(self, conn: serial.Serial):
        self.conn = conn

    def send_command(self, command):
        self.conn.write(bytes(command, 'utf-8'))
        self.conn.write(b'\xFF')
        self.conn.write(b'\xFF')
        self.conn.write(b'\xFF')
