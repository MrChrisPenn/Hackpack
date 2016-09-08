
"""
Written by @ncscomputing always inspired by:
David Whale
Martin O'Hanlon and Craig Richardson
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()


while True:

    mc.postToChat("Type in block number that you want?")
    block =int(input("Type here"))

    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,block)
    mc.postToChat("here is your block")
