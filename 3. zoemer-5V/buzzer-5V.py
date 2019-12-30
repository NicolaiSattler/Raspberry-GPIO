import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

BuzzerPin = 23
BuzzerState = False

GPIO.setup(BuzzerPin, GPIO.OUT)

while True:
    BuzzerState = not BuzzerState
    GPIO.output(BuzzerPin, BuzzerState)
    time.sleep(1)
