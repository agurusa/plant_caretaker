import spidev

SPI = spidev.SpiDev()
SPI.open(0,0)

class Sensor:
    def __init__(self, channel):
        self.channel = channel

    def getreading(self):
        # pull raw data from the chip
        rawdata = SPI.xfer([1, (8 + self.channel) << 4, 0])
        # process raw data
        processeddata = ((rawdata[1]&3 << 8) + rawdata[2])
        return processeddata
