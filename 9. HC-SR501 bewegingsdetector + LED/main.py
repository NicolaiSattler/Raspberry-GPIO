import RPi.GPIO as GPIO
import time as timer
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

SENSOR_PIN = 23
SENSOR_DELAY = 3
LED_PIN = 21


GPIO.setup(SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

count = 0

while True:
    motion = GPIO.input(SENSOR_PIN)
    
    if motion:
        datetimeNow = datetime.now().time()
        timeString = datetimeNow.strftime('%H:%M:%S')
        
        count = count + 1
        
        print('count:' + str(count) + ' time:' + timeString + ' - Motion detected')
        
        GPIO.output(LED_PIN, True)
        
        timer.sleep(SENSOR_DELAY)
        
        GPIO.output(LED_PIN, False)
        