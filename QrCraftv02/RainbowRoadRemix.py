import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time


mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

BlockIdsList=[1,2,7,21,22,31,46,49,73,80]

def SetRoadWool():
    count = 1
    pos = mc.player.getPos()
    while count <= 16:
        mc.setBlock(pos.x-count,pos.y-1,pos.z,35,count)
        count = count +1

def SetRoadRandom():
    count = 1
    pos = mc.player.getPos()
    while count <= 16:
        mc.setBlock(pos.x-count,pos.y-1,pos.z,random.choice(BlockIdsList))
        count = count +1


def main():
    
    mc.postToChat("Rainbow Road 2.0!")

    count = 0
    while count < 50:
        SetRoadWool()
        SetRoadRandom()
        time.sleep(0.4)
        count = count +1
    
