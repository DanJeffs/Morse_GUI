import RPi.GPIO as GPIO

def setup():
    #GPIO Setup and Config 
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)

    #initialize GPIO to low
    GPIO.output(17,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)

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

#Alphabet
def ledToggle(self):
    if GPIO.input(22):
        GPIO.output(22, GPIO.LOW)
    else:
        GPIO.output(22, GPIO.HIGH)