
"""
Written by @ncscomputing always inspired by:
David Whale
Martin O'Hanlon and Craig Richardson
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time
from sense_hat import SenseHat


sense = SenseHat()
mc = minecraft.Minecraft.create()


Block = 35
WoolIdList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
WallSize = 0



def PrintWall():
    WallSize = int(sense.get_temperature_from_humidity())
    msg = "Current Temp is: "+str(WallSize)
    mc.postToChat(msg)
    myList = [[0 for j in range(WallSize)]for i in range(WallSize)]
    #pos = mc.player.getTilePos()
    #mc.player.setPos(pos.x,pos.y,pos.z)

    for row in range (0,WallSize):
        for column in range (0,WallSize):
            mc.setBlock(pos.x+row,pos.y+column,pos.z-20,Block,random.choice(WoolIdList))
    return WallSize
def ClearWall(WallSize,blockID):
    myList = [[0 for j in range(WallSize)]for i in range(WallSize)]
    #pos = mc.player.getTilePos()
    #mc.player.setPos(pos.x,pos.y,pos.z)

    for row in range (0,WallSize):
        for column in range (0,WallSize):
            mc.setBlock(pos.x+row,pos.y+column,pos.z-20,blockID)

pos = mc.player.getTilePos()
while True:
    
    ClearWall(PrintWall(),0)
    time.sleep(1)
    
        
