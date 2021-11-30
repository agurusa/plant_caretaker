import waterpump as pump
import moisture_sense as ms
import time 

class Plant:
    def __init__(self, name, relay, sensor, dry_reading):
        self.name = name
        self.relay = pump.Pump(relay)
        self.sensor = ms.Sensor(sensor)
        self.moisture = self.sensor.getreading()
        self.dry_reading = dry_reading
        
    def dry(self):
        self.moisture = self.sensor.getreading()
        if self.moisture <= self.dry_reading:
            return True
        return False

    def water(self):
        # water for one second
        self.relay.on()
        time.sleep(1)
        self.relay.off()
