#written by @warksraspijam / @ncscomputing
#RGB colours taken from Scott Turner tutorial
#Basic Radio instructions taken from https://microbit-micropython.readthedocs.io/en/latest/tutorials/radio.html
#I used Codebug Glowbug neopixels. I assume it would work with most.

from microbit import *
import neopixel
np = neopixel.NeoPixel(pin0,1)

import radio
import random


def Red():
    np[0] = (255,0,0)#Red
    np.show()
    display.scroll('Red')
    sleep(3000)
    np.clear()

def Green():
    np[0] = (0,255,0)#Green
    np.show()
    display.scroll('Green')
    sleep(3000)
    np.clear()


while True:
    ColoursList = ['Red','Green']
     # Button A sends a "flash" message.
    Colour = random.choice(ColoursList)
    if button_a.was_pressed():
        radio.send(Colour) 
     # Read any incoming messages.
     incoming = radio.receive()
     if incoming == 'Green':
         Green()
     elif incoming == 'Red':
         Red()
