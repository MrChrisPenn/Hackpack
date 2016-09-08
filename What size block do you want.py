"""
Taken from the original idea by Craig Richardson in his 'Learning to program with Minecraft'
book. Adapted by @ncscomputing. 
"""


from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

block = 35
state = 0

def bigBlock(size,woolcolour):
    mc.setBlocks(pos.x, pos.y, pos.z,pos.x+size, pos.y+size, pos.z+size, 35,woolcolour)
    
def bigBlockClear(size,blockid):
    mc.setBlocks(pos.x, pos.y, pos.z,pos.x+size, pos.y+size, pos.z+size, blockid)

pos = mc.player.getTilePos()
while True:
    woolcolour = int(input("Type in a wool Id between 1-16"))
    size = int(input("Type the size of block you want"))
    bigBlock(size,woolcolour)
    time.sleep(10)
    bigBlockClear(size,0)
