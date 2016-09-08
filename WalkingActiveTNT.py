
"""
Written by @ncscomputing always inspired by:
David Whale
Martin O'Hanlon and Craig Richardson
"""


import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

#connect to minecraft
mc = minecraft.Minecraft.create()

#create list of some block ids to use later
#remix 2 active tnt
BlockId = 46#tnt

#set up loop
while True:
    
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z

    mc.setBlock(x,y-1,z,BlockId,1)# 1 means BOOM!
    time.sleep(0.2)
#Last time we walked random blocks now lets remix it :)
    
