import RPi.GPIO as GPIO
import time as timer

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN = 23

GPIO.setup(PIN, GPIO.IN)

lOld = not GPIO.input(PIN)

print('Light module started...')

while True:
    if GPIO.input(PIN) != lOld:
        if GPIO.input(PIN):
            print('\u263e')
        else:
            print('\u263c')
    lOld = GPIO.input(PIN)
    timer.sleep(0.2)
        
