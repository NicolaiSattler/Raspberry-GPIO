import RPi.GPIO as GPIO

from clock import SegmentClock 

class Main:

    def __init__(self):
        
        self.displayType = 0
        self.buttonPin = 13

        self.setBoardMode()
        self.setupButton()

        self.clock = SegmentClock()
        self.clock.setupPorts()
        self.clock.displayTemperature()

    def setBoardMode(self):
        GPIO.setmode(GPIO.BCM)

    #event is not being triggered. test if circuit is correct --> use led?
    def setupButton(self):
        GPIO.setup(self.buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.buttonPin, GPIO.RISING, callback=self.button_callback)

    def button_callback(self, channel):
        print('Button was pushed!')

Main()
