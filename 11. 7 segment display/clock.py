import RPi.GPIO as GPIO
import time
import os
from multiprocessing import Process, Value

from dht22 import DHT22 

class SegmentClock:

    def __init__(self):
        self.dotPort = 25
        self.segmentPorts = (11, 4 ,23, 8, 7, 10, 18)
        self.digitPorts = (22, 27, 17, 24)
        self.colonPorts = (5, 6)

        #more info: https://cdn-shop.adafruit.com/datasheets/1001datasheet.pdf
        self.numbers = {      
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
            '9' : (1, 1, 1, 1, 0, 1, 1),
            'A' : (1, 1, 1, 0, 1, 1, 1),
            'C' : (1, 0, 0, 1, 1, 1, 0),
            'E' : (1, 0, 0, 1, 1, 1, 1),
            'F' : (1, 0, 0, 0, 1, 1, 1),
            'H' : (0, 1, 1, 0, 1, 1, 1),
            'J' : (0, 1, 1, 1, 0, 0, 0),
            'L' : (0, 0, 0, 1, 1, 1, 0),
            'P' : (1, 1, 1, 0, 1, 1, 1),
       }
    

    def setupPorts(self):
        for item in self.segmentPorts:
            GPIO.setup(item, GPIO.OUT)
            GPIO.output(item, 0)
        
        for digit in self.digitPorts:
            GPIO.setup(digit, GPIO.OUT)
            GPIO.output(digit, 1)
        
        for item in self.colonPorts:
            GPIO.setup(item, GPIO.OUT)
            GPIO.output(item, 1)
        
        GPIO.setup(self.dotPort, GPIO.OUT)
        GPIO.output(self.dotPort, 1)
    
 
    def displayTime(self):
        GPIO.output(self.dotPort, 0 )

        try:
            while True:
                now = time.ctime()
                currentHourAndMinute = now[11:13] + now[14:16]
                s = str(currentHourAndMinute).rjust(4)
                secondIsEvent = int(now[18:19])%2 == 0
        
                for digit in range(4):
                    numberOfDigit = s[digit]
                    segmentActivityTuple = self.numbers[numberOfDigit]
                    digitPort = self.digitPorts[digit]
        
                    for seg in range(0, 7):
                        setPort = self.segmentPorts[seg]
                        onOff = segmentActivityTuple[seg]
        
                        GPIO.output(setPort, onOff)
        
                        if (secondIsEvent == True):
                            GPIO.output(6, 1)
                        else:
                            GPIO.output(6, 0)
        
        
                    GPIO.output(digitPort, 0)
        
                    time.sleep(0.0001)
        
                    GPIO.output(digitPort, 1)
        
        finally:
            GPIO.cleanup()
        
    def displayTemperature(self):
        sensor = DHT22()
        argument = Value('d', 10.0) 
        process = Process(target=sensor.read, args=(argument, ))
        process.start()

        try:
            print('start clock')

            while True:
                
                #print(argument.value)

                temp = str(argument.value)

                digitCount = len(temp)

                for digit in range(digitCount):
                    index = digit
                    
                    if digit == 1:
                        GPIO.output(self.dotPort, 1)
                    else:
                        GPIO.output(self.dotPort, 0)
                    
                    if digit == 2:
                        index = index + 1
    
                    numberOfDigit = temp[index]
                    segmentActivityTuple = self.numbers[numberOfDigit]
                    digitPort = self.digitPorts[digit]
    
                    for seg in range(0, 7):
                        setPort = self.segmentPorts[seg]
                        onOff = segmentActivityTuple[seg]
            
                        GPIO.output(setPort, onOff)
                    
                    GPIO.output(digitPort, 0)

                    time.sleep(0.001)

                    GPIO.output(digitPort, 1)
    
        except BaseException as e:
            print(e)
        finally:
            GPIO.cleanup()
        
