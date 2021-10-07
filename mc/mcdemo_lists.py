#Alex Plitt
#Places a randomly colored wool block
"""
Set up program for MC and two buttons
Create a 'counter' variable that starts at 0
Create a list of blockdata numbers for different color wool
Define a function called placeNext
 - It takes one arguement called direction
 - It changes the counter by adding the direction arguement
 - Place a wool block of the color from the list where the index matches the counter variable
 - If the counter is out of bounds of the index, reset it
In a forever loop:
 - If the first button was pressed, placeNext(1)
 - If the second button was pressed, placeNext(-1)
"""

import time
import RPi.GPIO as GPIO #Import Raspberry Pi GPIO library
GPIO.setwarnings(False) #Ignore warning for now
GPIO.setmode(GPIO.BCM) #Use physical pin numbering
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0

woolColor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def placeNext(direction):
    global counter
    counter += direction
    if counter > 14:
        counter = 0
    if counter < 0:
        counter = 14
    mc.setBlock(-20, 8, 43, 35, woolColor[counter])

while True:
    time.sleep(0.1)
    if GPIO.input(6) == GPIO.LOW:
        placeNext(1)
    if GPIO.input(13) == GPIO.LOW:
        placeNext(-1)