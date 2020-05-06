import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dotPort = 25
segmentPorts = (11, 4 ,23, 8, 7, 10, 18)
digitPorts = (22, 27, 17, 24)
colonPorts = (5, 6)
#more info: https://cdn-shop.adafruit.com/datasheets/1001datasheet.pdf
numbers = { 
        ' ' : (0, 0, 0, 0, 0, 0, 0),
        '0' : (1, 1, 1, 1, 1, 1, 0),
        '1' : (0, 1, 1, 0, 0, 0, 0),
        '2' : (1, 1, 0, 1, 1, 0, 1),
        '3' : (1, 1, 1, 1, 0, 0, 1),
        '4' : (0, 1, 1, 0, 0, 1, 1),
        '5' : (1, 0, 1, 1, 0, 1, 1),
        '6' : (1, 0, 1, 1, 1, 1, 1),
        '7' : (1, 1, 1, 0, 0, 0, 0),
        '8' : (1, 1, 1, 1, 1, 1, 1),
        '9' : (1, 1, 1, 1, 0, 1, 1)
        }

for item in segmentPorts:
    GPIO.setup(item, GPIO.OUT)
    GPIO.output(item, 0)

for digit in digitPorts:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)

for item in colonPorts:
    GPIO.setup(item, GPIO.OUT)
    GPIO.output(item, 1)

try:
    while True:
        now = time.ctime()
        currentHourAndMinute = now[11:13] + now[14:16]
        s = str(currentHourAndMinute).rjust(4)
        secondIsEvent = int(now[18:19])%2 == 0

        for digit in range(4):
            numberOfDigit = s[digit]
            onOffTuple = numbers[numberOfDigit]
            digitPort = digitPorts[digit]

            for seg in range(0, 7):
                setPort = segmentPorts[seg]
                onOff = onOffTuple[seg]

                GPIO.output(setPort, onOff)

                if (secondIsEvent == True):
                    GPIO.output(6, 1)
                else:
                    GPIO.output(6, 0)


            GPIO.output(digitPort, 0)

            time.sleep(0.001)

            GPIO.output(digitPort, 1)

finally:
    GPIO.cleanup()


                



