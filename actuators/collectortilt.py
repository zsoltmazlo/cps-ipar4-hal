import RPi.GPIO as GPIO
import time
from Adafruit_PCA9685 import PCA9685


class CollectorTilt:

    def __init__(self, pca9865_address=0x41, channel=0):
        self.MAX_ANGLE = 75
        self.MIN_ANGLE = 0
        self.DIFF = 5

        self.channel = channel
        self.expander = PCA9685(address=pca9865_address)
        self.expander.set_pwm_freq(60)
        self.pulse = 170
        self.angle = 0
        self.set_angle(0)

    def set_angle(self, angle):
        if angle > self.MAX_ANGLE or angle < self.MIN_ANGLE:
            return False, 0

        self.angle = angle

        prev_pulse = self.pulse
        self.pulse = int(self.angle/self.MAX_ANGLE*220.0+170)

        # we changing the angle with 5 diff
        while abs(prev_pulse-self.pulse) > self.DIFF:
            prev_pulse += self.DIFF if self.pulse > prev_pulse else -self.DIFF
            self.expander.set_pwm(self.channel, 0, int(prev_pulse))
            time.sleep(0.05)

        # finishing setup with the actual value
        self.expander.set_pwm(0, 0, self.pulse)
        return True, self.angle

    def get_angle(self):
        return True, self.angle

    def finish(self):
        self.set_angle(0)


