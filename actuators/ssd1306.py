import socket
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from threading import Lock
import time

from PIL import ImageFont


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
        self.draw.font = ImageFont.truetype('/home/pi/cps-gen2/Minecraftia-Regular.ttf', 8)

        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.display.width, self.display.height), outline=0, fill=0)

    def show_connection_details(self, port):
        self.mutex.acquire()
        self.draw.rectangle((0,0,14,14), fill=255, outline=255)
        self.draw.text((3, 2), "IP", fill=0)
        self.draw.rectangle((14, 0, 127, 14), fill=0, outline=255)
        self.draw.text((18, 2), self.__get_ip_address()+":"+str(port), fill=255)
        self.display.image(self.image)
        try:
            self.display.display()
        except OSError:
            print("OS error during display content on SSD1306, SSD1306::show_connection_details")
            return False
        finally:
            self.mutex.release()
        return True

    def show_message_box(self):
        self.mutex.acquire()
        self.draw.rectangle((0, 16, 127, 63), fill=0, outline=255)
        self.draw.rectangle((0, 16, 127, 28), fill=255, outline=255)
        self.draw.text((3, 17), "MESSAGE", fill=0)

        try:
            self.display.display()
        except OSError:
            print("OS error during display content on SSD1306, SSD1306::show_message_box")
            return False
        finally:
            self.mutex.release()
        return True

    def show_message(self, message):
        self.mutex.acquire()
        self.draw.rectangle((2, 36, 126, 62), fill=0, outline=0)

        y = 30
        chunks = message.split(' ')
        line = ''
        for chunk in chunks:
            if '\n' in chunk:
                chunks2 = chunk.split('\n')
                line += chunks2[0]
                self.draw.text((3, y), line, fill=255)
                y += 10
                line = ''
                chunk = chunks2[1]

            if len(line)+len(chunk) > 25:
                self.draw.text((3, y), line, fill=255)
                y += 10
                line = ''
            line += chunk
            line += ' '
        self.draw.text((3, y), line, fill=255)
        self.display.image(self.image)
        try:
            self.display.display()
        except OSError:
            print("OS error during display content on SSD1306, SSD1306::show_message")
            return False
        finally:
            self.mutex.release()
        return True

    def change_connected_status(self, connected=False):
        self.mutex.acquire()
        self.draw.rectangle((114, 2, 124, 12), fill=0, outline=0)
        f = 255 if connected else 0
        self.draw.ellipse((116, 3, 124, 11), fill=f, outline=f)
        self.display.image(self.image)
        try:
            self.display.display()
        except OSError:
            print("OS error during display content on SSD1306, SSD1306::change_connected_status")
            return False
        finally:
            self.mutex.release()
        return True

    def draw_text(self, x, y, text):
        self.mutex.acquire()
        self.draw.text((x, y), text, fill=255)
        self.display.image(self.image)
        try:
            self.display.display()
        except OSError:
            print("OS error during display content on SSD1306, SSD1306::draw_text")
            return False
        finally:
            self.mutex.release()
        return True

    def clear(self, x=0, y=0, w=128, h=64, f=0):
        self.mutex.acquire()
        self.draw.rectangle((x, y, x + w, y + h), outline=0, fill=f)
        self.display.image(self.image)
        try:
            self.display.display()
        except OSError:
            print("OS error during display content on SSD1306, SSD1306::clear")
            return False
        finally:
            self.mutex.release()
        return True

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
        try:
            self.display.display()
        except OSError:
            print("OS error during display content on SSD1306, SSD1306::alert")
            return False
        finally:
            self.mutex.release()
        return True

    def __get_ip_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
