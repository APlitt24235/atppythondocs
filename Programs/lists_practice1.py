#Alex Plitt
#Lists Practice 1

#A variable that holds more than 1 value is a list
 #groceries = ["Bread", "Milk", "Eggs", "Cheese"]
#You can get items from a list from their index
 #print(groceries[0])

#Start an empty list
 #cart = []

#For every item in my grocery list, add that item to the cart
 #for item in groceries:
     #cart.append(item)
 #print(cart)

import random
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    funnyQuotes = ["Lamborghini", "Genie", "Bikini", "Beanie", "Weenie", "Zucchini", "Linguini"]
    randomNumber = random.randint(0, 6)
    time.sleep(0.1)
    if GPIO.input(6) == GPIO.LOW:
        print("Here in my garage with my brand new " + funnyQuotes[randomNumber] + ". But you know what I like more than my " + funnyQuotes[randomNumber] + ". KNOWLEDGE.")