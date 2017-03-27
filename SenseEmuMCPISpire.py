"""
Code taken from Craig Richardson's 'Learning to program Python with Minecraft' book 
and adapted by @ncscomputing to work with Sensehat :) go buy his book :)
 
"""

from mcpi.minecraft import Minecraft
import time
from sense_emu import SenseHat

sense = SenseHat()
mc = Minecraft.create()


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z+4

height = 0
block = 35


def Spire():
    woolColour = 1
    while True:
        height =int(sense.temp)
        # Spire sides: should be same as height
        sideHeight = height
        mc.setBlocks(x + 1, y, z + 1, x + 3, y + sideHeight - 1, z + 3, block,woolColour)

        # Spire point: should be two times the height
        pointHeight = height * 2
        mc.setBlocks(x + 2, y, z + 2, x + 2, y + pointHeight - 1, z + 2, block,woolColour)

        # Spire base: should be half the height
        baseHeight = height / 2
        mc.setBlocks(x, y, z, x + 4, y + baseHeight - 1, z + 4, block,woolColour)

        time.sleep(6)

        woolColour = woolColour +1
        height = height +1
        
Spire()
