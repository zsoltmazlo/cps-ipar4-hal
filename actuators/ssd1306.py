import socket
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from threading import Lock
import time


class SSD1306:

    def __init__(self):
        self.display = Adafruit_SSD1306.SSD1306_128_64(rst=None)
        self.mutex = Lock()
        self.display.begin()
        self.display.clear()
        self.display.display()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        self.image = Image.new('1', (self.display.width, self.display.height))

        # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)

        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.display.width, self.display.height), outline=0, fill=0)

    def show_connection_details(self, port):
        self.mutex.acquire()
        self.draw.rectangle((0,0,16,16), fill=255, outline=255)
        self.draw.text((3, 3), "IP", fill=0)
        self.draw.rectangle((16, 0, 127, 16), fill=0, outline=255)
        self.draw.text((22, 3), self.__get_ip_address()+":"+str(port), fill=255)
        self.display.image(self.image)
        try:
            self.display.display()
        except OSError:
            print("OS error during display content on SSD1306, draw_text")
        self.mutex.release()


    def change_connected_status(self, connected=False):
        self.mutex.acquire()
        self.draw.rectangle((114, 3, 124, 12), fill=0, outline=0)
        f = 255 if connected else 0
        self.draw.ellipse((115, 4, 123, 12), fill=f, outline=f)
        self.display.image(self.image)
        try:
            self.display.display()
        except OSError:
            print("OS error during display content on SSD1306, draw_text")
        self.mutex.release()

    def draw_text(self, x, y, text):
        self.mutex.acquire()
        self.draw.text((x, y), text, fill=255)
        self.display.image(self.image)
        try:
            self.display.display()
        except OSError:
            print("OS error during display content on SSD1306, draw_text")
        self.mutex.release()

    def clear(self, x=0, y=0, w=128, h=64, f=0):
        self.mutex.acquire()
        self.draw.rectangle((x, y, x + w, y + h), outline=0, fill=f)
        self.display.image(self.image)
        try:
            self.display.display()
        except OSError:
            print("OS error during display content on SSD1306, draw_text")
        self.mutex.release()

    def alert(self, text, timeout=3.0):
        self.mutex.acquire()

        # create new image for the alert and show only that
        image = Image.new('1', (self.display.width, self.display.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, self.display.width, self.display.height), outline=0, fill=0)
        draw.text((0, 0), text, fill=255)
        self.display.image(image)
        self.display.display()
        time.sleep(timeout)

        # show previously saved image
        self.display.image(self.image)
        self.display.display()

        self.mutex.release()

    def __get_ip_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]