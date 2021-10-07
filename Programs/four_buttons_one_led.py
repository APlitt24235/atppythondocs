#Alex Plitt
#Four Buttons, One LED

#Use a module for requesting data online
import requests

#Use a module to control time
import time

#Setup for buttons and LEDs
import RPi.GPIO as GPIO #Import Raspberry Pi GPIO library
GPIO.setwarnings(False) #Ignore warning for now
GPIO.setmode(GPIO.BCM) #Use physical pin numbering

#Set up each pin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Start an infinite loop
while True:
    #Wait for 1 second
    time.sleep(1)
    #Check the first button
    if GPIO.input(6) == GPIO.LOW:
        print("Button 6 was pressed!")
        requests.get("http://192.168.10.53:5000/sfx?file=tacoBell")
    elif GPIO.input(13) == GPIO.LOW:
        print("Button 13 was pressed!")
    elif GPIO.input(19) == GPIO.LOW:
        print("Button 19 was pressed!")
    elif GPIO.input(26) == GPIO.LOW:
        print("Button 26 was pressed!")
            