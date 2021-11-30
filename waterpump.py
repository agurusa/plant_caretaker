from RPi import GPIO

OFF = 1
ON = 0

GPIO.setmode(GPIO.BOARD)

CHANNEL_MAP = {1: 11,
               2: 13,
               3: 29,
               4: 31}


class Pump:
    def __init__(self, channel):
        self.pin = CHANNEL_MAP[channel]
        GPIO.setup(self.pin, GPIO.OUT)
        self.turnoff()

    def off(self):
        GPIO.output(self.pin, OFF)

    def on(self):
        GPIO.output(self.pin, ON)
