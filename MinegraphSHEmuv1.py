"""
Written by @ncscomputing v2 to work  with Pi Sense hat emulator on Pi not web based.
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
from sense_emu import SenseHat

sense = SenseHat()

mc = minecraft.Minecraft.create()
orx,ory,orz = mc.player.getPos()

mc.postToChat("Start Graph")

blockTypeList=[35,45,3,4,5,6]
DataStreamList = []

DataStreamCount= 0

def BuildDataBlock():
    temp = int(sense.temp)
    DataStreamList.append(temp)
    orx,ory,orz = mc.player.getPos()
    block = random.choice(blockTypeList)

    for i in range (0,temp):
        x,y,z = mc.player.getPos()
        mc.setBlock(x,i,z,block)
    mc.player.setPos(orx,ory,orz+1)
    msg = "Temp currently is:",temp 
    print(msg)
        
while True:
    BuildDataBlock()
    time.sleep(4)
