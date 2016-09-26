# autotorch.py  31/01/2015  D.J.Whale
#
# Show how to turn torches on and off automatically.
# Builds the turner prize "room with a light going on and off"
# Stand in the room, and the lights go on and off.
# Stand outside the room, and they don't (or do they?!)


#-------------Adapted and messed around with by @ncscomputing / @warksraspijam


import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
FLASH_TIME = 1.0
WIDTH = 10
DEPTH = 10
HEIGHT = 10

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
ROOM_X = pos.x + 2
ROOM_Y = pos.y
ROOM_Z = pos.z

def buildWall():#WIDTH,HEIGHT):
    Block = 35
    WoolIdList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    myList = [[0 for j in range(8)]for i in range(8)]


    #pos = mc.player.getTilePos()
    #mc.player.setPos(pos.x,pos.y,pos.z)

    for row in range (0,8):
        for column in range (0,8):
            mc.setBlock(ROOM_X+row,ROOM_Y+column,ROOM_Z+1,Block,random.choice(WoolIdList))


def buildRoom():
    """Build a cube room with a door"""
    # build a cube
    mc.setBlocks(ROOM_X, ROOM_Y, ROOM_Z, ROOM_X+WIDTH, ROOM_Y+HEIGHT, ROOM_Z+DEPTH, 35,1)#orange

    # carve out the inside
    mc.setBlocks(ROOM_X+1, ROOM_Y, ROOM_Z+1, ROOM_X+WIDTH-2, ROOM_Y+HEIGHT-1, ROOM_Z+DEPTH-2,0)
    
    # carve out a face
    #eyes
    mc.setBlock(ROOM_X+(WIDTH/2)-2,ROOM_Y+HEIGHT-3, ROOM_Z,block.AIR.id)#right eye
    mc.setBlock(ROOM_X+(WIDTH/2)+2,ROOM_Y+HEIGHT-3, ROOM_Z,block.AIR.id)#left eye
    mc.setBlock(ROOM_X+(WIDTH/2),ROOM_Y+HEIGHT-6, ROOM_Z,block.AIR.id)#nose

    mc.setBlocks(ROOM_X+2,ROOM_Y+HEIGHT-8, ROOM_Z,ROOM_X+7,ROOM_Y+HEIGHT-8, ROOM_Z,block.AIR.id)#mouth


def destroyRoom():
    """Remove all traces of the room"""
    # build cube out of air
    mc.setBlocks(ROOM_X, ROOM_Y, ROOM_Z, ROOM_X+WIDTH, ROOM_Y+HEIGHT, ROOM_Z+DEPTH, block.AIR.id)


nexttime = None

# GAME LOOP
try:
    buildRoom()

    while True:
        time.sleep(0.1)
        buildWall()
    
finally:
    destroyRoom()

# END
