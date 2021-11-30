from RPi import GPIO

RELAY1 = 11
RELAY2 = 13
RELAY3 = 29
RELAY4 = 31

RELAYS = [RELAY1, RELAY2, RELAY3, RELAY4]
OFF = 1
ON = 0

GPIO.setmode(GPIO.BOARD)

    
CHANNEL_MAP ={1: 11,
 2: 13,
 3: 29,
 3: 31}

class Pump:
    def __init__(self, channel):
        self.pin = CHANNEL_MAP[channel]
        GPIO.setup(self.pin, GPIO.OUT)
        self.turnoff()

    def turnoff(self):
        GPIO.output(self.pin, OFF)

    def turnon(self):
        GPIO.output(self.pin, ON)


        
        
        
