# Write your code here :-)
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 21
ledState = False

GPIO.setup(LED, GPIO.OUT)

while True:
    ledState = not ledState
    GPIO.output(LED, ledState)
    time.sleep(0.1)