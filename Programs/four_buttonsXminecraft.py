#Alex Plitt
#Four Buttons X Minecraft

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import requests
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    time.sleep(0.1)
    if GPIO.input(6) == GPIO.LOW:
        requests.get("http://192.168.10.53:5000/tutd?thumb=up")
    elif GPIO.input(13) == GPIO.LOW:
        requests.get("http://192.168.10.53:5000/tutd?thumb=oops")
    elif GPIO.input(19) == GPIO.LOW:
        mc.player.setTilePos(25,64,88)
    elif GPIO.input(26) == GPIO.LOW:
        playerPosition = mc.player.getTilePos()
        mc.postToChat(playerPosition)
        