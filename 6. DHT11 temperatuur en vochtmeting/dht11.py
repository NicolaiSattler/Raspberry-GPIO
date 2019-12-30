import sys
import RPi.GPIO as GPIO
import Adafruit_DHT
import time as timer

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

i = 0

while True:
    humidity, tempature = Adafruit_DHT.read_retry(11, 23)
    
    if humidity is not None and tempature is not None:
        print('{0} - Tempature={0.0.1F}*C Humidity={1:0.1f}%'.format(i, tempature, humidity)) 
    else:
        print('{0} - Failed to read data from the sensors. Please try again.'.format(i))
    
    i+=1
    timer.sleep(1)