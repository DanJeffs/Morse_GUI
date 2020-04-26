
import RPi.GPIO as GPIO

    #Functions for LED interactions
def redLed(self):
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(17,GPIO.LOW)

def yellowLed(self):
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(22,GPIO.LOW)
    GPIO.output(17,GPIO.LOW)

def allOn(self):
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)

def allOff(self):
    GPIO.output(17,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)

def greenLed(self):
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(22,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)
