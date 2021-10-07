#Alex Plitt
#Minecraft Code Example

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("Hello!")

playerPosition = mc.player.getTilePos()
mc.postToChat(playerPosition)