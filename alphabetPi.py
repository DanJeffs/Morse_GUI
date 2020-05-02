import PiLeds as led
import time

#Define times for Morse Code beeper 
ditTime = 0.1;
dashTime = ditTime * 3;
spaceTime = ditTime * 7;

def dit(self):
    led.ledToggle(self)
    time.sleep(ditTime)
    led.ledToggle(self)
    time.sleep(ditTime)

def dash(self):    
    led.ledToggle(self)
    time.sleep(dashTime)
    led.ledToggle(self)
    time.sleep(ditTime)

def space(self):
    time.sleep(spaceTime)

def newLetter(self):
    time.sleep(dashTime)

#    "A" : ".-"
def A(self):
    dit(self)
    dash(self)
#    "B" : "-...",
def B(self):
    dash(self)
    dit(self)
    dit(self)
    dit(self)
#    "C" : "-.-.",
def C(self):
    dash(self)
    dit(self)
    dash(self)
    dit(self)
#    "D" : "-..",
def D(self):
    dash(self)
    dit(self)
    dit(self)
#    "E" : ".",
def E(self):
    dit(self)
#    "F" : "..-.",
def F(self):
    dit(self)
    dit(self)
    dash(self)
    dit(self)
#    "G" : "--.",
def G(self):
    dash(self)
    dash(self)
    dit(self)
#    "H" : "....",
def H(self):
    dit(self)
    dit(self)
    dit(self)
    dit(self)
#    "I" : "..",
def I(self):
    dit(self)
    dit(self)
#    "J" : ".---",
def J(self):
    dit(self)
    dash(self)
    dash(self)
    dash(self)
#    "K" : "-.-",
def K(self):
    dash(self)
    dit(self)
    dash(self)
#    "L" : ".-..",
def L(self):
    dit(self)
    dash(self)
    dit(self)
    dit(self)
#    "M" : "--",
def M(self):
    dash(self)
    dash(self)
#    "N" : "-.",
def N(self):
    dash(self)
    dit(self)
#    "O" : "---",
def O(self):
    dash(self)
    dash(self)
    dash(self)
#    "P" : ".--.",
def P(self):
    dit(self)
    dash(self)
    dash(self)
    dit(self)
#    "Q" : "--.-",
def Q(self):
    dash(self)
    dash(self)
    dit(self)
    dash(self)
#    "R" : ".-.",
def R(self):
    dit(self)
    dash(self)
    dit(self)
#    "S" : "...",
def S(self):
    dit(self)
    dit(self)
    dit(self)
#    "T" : "-",
def T(self):
    dash(self)
#    "U" : "..-",
def U(self):
    dit(self)
    dit(self)
    dash(self)
#    "V" : "...-",
def V(self):
    dit(self)
    dit(self)
    dit(self)
    dash(self)
#    "W" : ".--",
def W(self):
    dit(self)
    dash(self)
    dash(self)
#    "X" : "-..-",
def X(self):
    dash(self)
    dit(self)
    dit(self)
    dash(self)
#    "Y" : "-.--",
def Y(self):
    dash(self)
    dit(self)
    dash(self)
    dash(self)
#    "Z" : "--..",
def Z(self):
    dash(self)
    dash(self)
    dit(self)
    dit(self)
