import Adafruit_DHT
import time

class DHT22:

    def __init__(self):
        self.dht22port = 16
        self.dht_sensor = Adafruit_DHT.DHT22

    def read(self, temp):

        previousTemp = 0.0

        while True:
            h, t = Adafruit_DHT.read_retry(self.dht_sensor, self.dht22port)
            
            if (type(t) is float):
                newTemp = round(t, 2)

                if newTemp != previousTemp:
                    previousTemp = newTemp
                    temp.value = newTemp
                    time.sleep(30)
            else:
                lt = time.asctime(time.localtime(time.time()))
                print(f"{lt}, no float was supplied. {t}")


