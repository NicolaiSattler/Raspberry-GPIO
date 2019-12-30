import RPi.GPIO as GPIO
import time as timer

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

BuzzerPin = 23
BuzzerState = False

GPIO.setup(BuzzerPin, GPIO.OUT)

def buzz(frequency, duration):
    halfWaveTime = 1 / (frequency * 2)
    waves = int(duration * frequency)
    
    for i in range(waves):
        GPIO.output(BuzzerPin, True)
        timer.sleep(halfWaveTime)
        GPIO.output(BuzzerPin, False)
        timer.sleep(halfWaveTime)

def play(notes, durations):
    t = 0
 
    for n in notes:
        duration = durations[t]
        buzz(n, duration)
        noteStop = duration * 0.1
        timer.sleep(noteStop)
        t+=1

def getVaderJacobNotes():
    return [262,294,330,262,262,294,330,262,330,349,392,330,349,392,392,440,392,349,330,262,392,440,392,349,330,262,262,196,262,262,196,262262,294,330,262,262,294,330,262,330,349,392,330,349,392,392,440,392,349,330,262,392,440,392,349,330,262,262,196,262,262,196,262]

def getVaderJacobNoteDurations():
    return [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,1,0.25,0.25,0.25,0.25,0.5,0.5,0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5,1,0.5,0.5,1]

def playVaderJacob():
    notes = getVaderJacobNotes()
    noteDurations = getVaderJacobNoteDurations()
    play(notes, noteDurations)

#buzz(262, 0.5)
#play()    
playVaderJacob()
            