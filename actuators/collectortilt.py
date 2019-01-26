import RPi.GPIO as GPIO
import time


class CollectorTilt:

    def __init__(self, board_pin=12, bcm_pin=18):
        try:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(board_pin, GPIO.OUT)
            self.pwm = GPIO.PWM(board_pin, 100)
            self.should_cleanup = True
        except ValueError:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(bcm_pin, GPIO.OUT)
            self.pwm = GPIO.PWM(bcm_pin, 100)
            self.should_cleanup = False

        self.pwm.start(0)
        self.duty_cycle = 6
        self.set_angle(0)

    def set_angle(self, angle):
        if angle > 85 or angle < 0:
            return False, 0

        self.angle = angle

        prev_duty_cycle = self.duty_cycle
        self.duty_cycle = 6+angle/85.0*8.5

        # we changing the angle with 0.1 diff
        times = int(abs(self.duty_cycle-prev_duty_cycle)*10)
        diff = 0.1 if self.duty_cycle > prev_duty_cycle else -0.1;
        for i in range(0, times):
            prev_duty_cycle += diff
            self.pwm.ChangeDutyCycle(prev_duty_cycle)
            time.sleep(0.05)

        # finishing setup with the actual value
        self.pwm.ChangeDutyCycle(self.duty_cycle)
        return True, self.angle

    def get_angle(self):
        return True, self.angle

    def finish(self):
        self.set_angle(0)
        self.pwm.stop()
        if self.should_cleanup:
            GPIO.cleanup()

