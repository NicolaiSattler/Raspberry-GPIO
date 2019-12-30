import RPi.GPIO as GPIO
import time as timer
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN = 23

GPIO.setup(PIN, GPIO.IN)

while True:
    motion = GPIO.input(PIN)
    
    if motion:
        datetimeNow = datetime.now().time()
        timeString = datetimeNow.strftime('%H:%M:%S')
        
        print(timeString + ' - Motion detected')
    
    timer.sleep(1)