#Alex Plitt
#MC Demo: Place Blocks/House with a button

import RPi.GPIO as GPIO #Import Raspberry Pi GPIO library
GPIO.setwarnings(False) #Ignore warning for now
GPIO.setmode(GPIO.BCM) #Use physical pin numbering
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buildHouse(x, y, z):
    mc.setBlocks(x, y, z, x, y + 3, z + 6, 5) #Right Wall
    mc.setBlocks(x + 1, y, z + 6, x + 4, y + 3, z + 6, 5) #Back Wall
    mc.setBlocks(x + 4, y, z, x + 4, y + 3, z + 5, 5)#Left Wall
    mc.setBlocks(x + 1, y, z, x + 3, y + 3, z, 5)#Front Wall
    mc.setBlocks(x + 1, y + 3, z + 1, x + 3, y + 3, z + 5, 5)#Ceiling
    mc.setBlocks(x + 2, y, z, x + 2, y + 1, z, 0)#Front Door Opening
    mc.setBlocks(x, y - 1, z, x + 4, y - 1, z + 6, 5)#Floor
    mc.setBlocks(x, y + 1, z + 2, x, y + 1, z + 4, 20)#Windows
    mc.setBlock(x + 2, y + 1, z + 5, 50)#Torch
    mc.setBlock(x + 2, y, z + 5, 54)#Chest
    mc.setBlock(x + 3, y, z + 5, 58)#Crafting Table
    mc.setBlock(x + 1, y, z + 5, 61)#Furnace

while True:
    playerPosition = mc.player.getTilePos()
    if GPIO.input(6) == GPIO.LOW:
        buildHouse(playerPosition.x, playerPosition.y, playerPosition.z)

