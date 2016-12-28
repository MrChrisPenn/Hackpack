from guizero import *

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
"""
Written by @ncscomputing always inspired by:
David Whale
Martin O'Hanlon and Craig Richardson
"""

mc = minecraft.Minecraft.create()


WoolIds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


def dropTNT():
  mc.postToChat("TNT laid")
  pos = mc.player.getPos()
  x = pos.x
  y = pos.y
  z = pos.z
  mc.setBlock(x,y-1,z,46,1)# 1 means BOOM!

def dropGlass():
  mc.postToChat("Glass laid")
  pos = mc.player.getPos()
  x = pos.x
  y = pos.y
  z = pos.z
  mc.setBlock(x,y-1,z,20)

def dropWOOL():
  print("Random Wool laid")
  pos = mc.player.getPos()
  x = pos.x
  y = pos.y
  z = pos.z
  mc.setBlock(x,y-1,z,35,random.choice(WoolIds))
  


app = App()
buttonTNT = PushButton(app,dropTNT,text="TNT")
buttonGLASS = PushButton(app,dropGlass,text="GLASS")
buttonWOOL = PushButton(app,dropWOOL,text="Random WOOL")

app.display()
