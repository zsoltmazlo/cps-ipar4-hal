import time
from Adafruit_PCA9685 import PCA9685


class ServoController:

    def __init__(self, expander, channel, min_angle, max_angle, min_pulse, max_pulse):
        self.DIFF = 10
        self.max_pulse = max_pulse
        self.min_pulse = min_pulse
        self.max_angle = max_angle
        self.min_angle = min_angle
        self.channel = channel
        self.expander = expander
        self.angle = self.min_angle
        self.pulse = self.min_pulse

    def set_angle(self, angle):
        if angle > self.max_angle or angle < self.min_angle:
            return False, 0

        self.angle = angle
        prev_pulse = self.pulse
        self.pulse = int(self.angle / self.max_angle * (self.max_pulse-self.min_pulse) + self.min_pulse)

        # we changing the angle with 5 diff
        while abs(prev_pulse-self.pulse) > self.DIFF:
            prev_pulse += self.DIFF if self.pulse > prev_pulse else -self.DIFF
            self.expander.set_pwm(self.channel, 0, int(prev_pulse))
            time.sleep(0.05)

        # finishing setup with the actual value
        self.expander.set_pwm(self.channel, 0, self.pulse)
        return True, self.angle

    def get_angle(self):
        return self.angle


class CollectorPositioner:

    def __init__(self, pca9865_address=0x41, tilt_servo_ch=None, rotation_servo_ch=None):
        # TODO add output enable functionality
        try:
            self.expander = PCA9685(address=pca9865_address)
            self.expander.set_pwm_freq(60)
            if tilt_servo_ch is not None:
                self.tilt_servo = ServoController(
                    expander=self.expander,
                    channel=tilt_servo_ch,
                    min_angle=0,
                    max_angle=90,
                    # min_pulse=170,
                    # max_pulse=390
                    min_pulse=140,
                    max_pulse=340
                )
                self.tilt_servo.set_angle(0)
            else:
                self.tilt_servo = None

            if rotation_servo_ch is not None:
                self.rotation_servo = ServoController(
                    expander=self.expander,
                    channel=rotation_servo_ch,
                    min_angle=0,
                    max_angle=180,
                    min_pulse=180,
                    max_pulse=660
                )
                self.rotation_servo.set_angle(0)
            else:
                self.rotation_servo = None
        except:
            self.expander = None
            self.tilt_servo = None
            self.rotation_servo = None
            print("Collector positioner could not initiated")

    def set_tilt_angle(self, angle):
        if self.tilt_servo is None:
            return False, 0
        else:
            return self.tilt_servo.set_angle(angle)

    def get_tilt_angle(self):
        if self.tilt_servo is None:
            return False, 0
        else:
            return True, self.tilt_servo.get_angle()

    def set_rotation_angle(self, angle):
        if self.rotation_servo is None:
            return False, 0
        else:
            return self.rotation_servo.set_angle(angle)

    def get_rotation_angle(self):
        if self.rotation_servo is None:
            return False, 0
        else:
            return True, self.rotation_servo.get_angle()

    def finish(self):
        if self.tilt_servo is not None:
            self.tilt_servo.set_angle(0)
        if self.rotation_servo is not None:
            self.rotation_servo.set_angle(0)


