import os
import time
import Adafruit_DHT

SENSOR = Adafruit_DHT.DHT22
PIN = 4
currentDirectory = os.getcwd()
fileName = currentDirectory + "/sensordata.csv"

try:
    f = open(fileName, "a+")

    if os.stat(fileName).st_size == 0:
        f.write('Date,Time,Temperature,Humidity\r\n')
except:
    pass

while True:
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)

    if humidity is not None and temperature is not None:
        row = f"{time.strftime('%m/%d/%y')},{time.strftime('%H:%M')},{round(temperature,1)}*C,{round(humidity, 0)}%" + "\r\n"
        f.write(row)
        print(row)
    else:
        print("Failed to retrieve data from sensor")

    time.sleep(300)
