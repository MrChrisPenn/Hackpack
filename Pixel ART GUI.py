import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time



##
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
  



##




#written by @ncscomputing / @warksraspijam

BlocksList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
WoolList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
mc = minecraft.Minecraft.create()
def hello():
    print("hello")

def StarTrooper(B1,B2):
    row0 = [B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1]
    row1 = [B1,B1,B1,B1,B1,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1]
    row2 = [B1,B1,B1,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1,B1,B1,B1,B1]
    row3 = [B1,B1,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1,B1,B1,B1]
    row4 = [B1,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1,B1,B1]
    row5 = [B1,B1,B1,B1,B2,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B2,B1,B1,B1,B1,B1,B1,B1]
    row6 = [B1,B1,B1,B1,B2,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B2,B1,B1,B1,B1,B1,B1,B1]
    row7 = [B1,B1,B1,B1,B2,B2,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B2,B2,B1,B1,B1,B1,B1,B1,B1]
    row8 = [B1,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1,B1,B1]
    row9 = [B1,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1,B1,B1]
    row10 =[B1,B1,B1,B1,B2,B2,B1,B1,B1,B1,B1,B1,B1,B2,B1,B1,B1,B1,B1,B1,B1,B2,B2,B1,B1,B1,B1,B1,B1,B1]
    row11 =[B1,B1,B1,B1,B2,B2,B1,B1,B1,B1,B1,B1,B2,B2,B2,B1,B1,B1,B1,B1,B1,B2,B2,B1,B1,B1,B1,B1,B1,B1]
    row12 =[B1,B1,B1,B1,B2,B2,B1,B1,B1,B1,B1,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1,B2,B2,B1,B1,B1,B1,B1,B1,B1]
    row13 =[B1,B1,B1,B2,B2,B2,B1,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B2,B2,B2,B1,B1,B1,B1,B1,B1]
    row14 =[B1,B1,B2,B2,B2,B2,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B2,B1,B2,B2,B1,B1,B1,B1,B1]
    row15 =[B1,B1,B2,B2,B2,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B2,B2,B1,B1,B1,B1,B1]
    row16 =[B1,B1,B2,B2,B2,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B2,B2,B1,B1,B1,B1,B1]
    row17 =[B1,B1,B2,B2,B2,B1,B2,B2,B2,B2,B2,B2,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B1,B2,B2,B1,B1,B1,B1,B1]
    row18 =[B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1]
    row19 =[B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B2,B2,B2,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1]
    rowB2 =[B1,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B2,B2,B2,B2,B2,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1]
    row21 =[B1,B2,B2,B2,B2,B2,B2,B2,B1,B1,B2,B2,B2,B2,B2,B2,B2,B1,B1,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1]
    row22 =[B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1]
    row23 =[B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1]
    row24 =[B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B2,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1]
    row25= [B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B2,B1,B1,B2,B2,B2,B2,B2,B1,B1,B2,B2,B1,B1,B1,B1,B1]
    row26= [B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1,B1]
    row27= [B1,B1,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1,B1,B1]
    row28 =[B1,B1,B1,B1,B1,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1,B1,B1]
    row29 =[B1,B1,B1,B1,B1,B1,B1,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1,B2,B2,B2,B2,B2,B1,B1,B1,B1,B1,B1,B1,B1]
    row30 =[B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1]
    TempList = [row30,row29,row28,row27,row26,row25,row24,row23,row22,row21,rowB2,row19,row18,row17,row16,row15,row14,row13,row12,row11,row10,row9,row8,row7,row6,row5,row4,row3,row2,row1,row0]
    return TempList

def RandomStormy(B1,BlocksList):
    row0 = [B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1]
    row1 = [B1,B1,B1,B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1]
    row2 = [B1,B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1,B1,B1]
    row3 = [B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1,B1]
    row4 = [B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1]
    row5 = [B1,B1,B1,B1,(random.choice(BlocksList)),B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1]
    row6 = [B1,B1,B1,B1,(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1]
    row7 = [B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1]
    row8 = [B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1]
    row9 = [B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1]
    row10 =[B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1,(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1]
    row11 =[B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1]
    row12 =[B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1]
    row13 =[B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1]
    row14 =[B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,(random.choice(BlocksList)),B1,(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1]
    row15 =[B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1]
    row16 =[B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1]
    row17 =[B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1]
    row18 =[B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1]
    row19 =[B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1]
    row20 =[B1,(random.choice(BlocksList)),B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1]
    row21 =[B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1]
    row22 =[B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1]
    row23 =[B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1]
    row24 =[B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,(random.choice(BlocksList)),B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1]
    row25= [B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,(random.choice(BlocksList)),B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1]
    row26= [B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1]
    row27= [B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1]
    row28 =[B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1]
    row29 =[B1,B1,B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),B1,B1,B1,B1,B1,B1,B1,B1]
    row30 =[B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1]
    TempList = [row30,row29,row28,row27,row26,row25,row24,row23,row22,row21,row20,row19,row18,row17,row16,row15,row14,row13,row12,row11,row10,row9,row8,row7,row6,row5,row4,row3,row2,row1,row0]
    return TempList

def RandomWall():
    row0 = [(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row1 = [(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row2 = [(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row3 = [(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row4 = [(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row5 = [(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row6 = [(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row7 = [(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row8 = [(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row9 = [(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row10 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row11 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row12 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row13 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row14 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row15 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row16 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row17 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row18 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row19 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row20 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row21 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row22 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row23 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row24 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row25= [(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row26= [(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row27= [(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row28 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row29 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    row30 =[(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList)),(random.choice(BlocksList))]
    TempList = [row30,row29,row28,row27,row26,row25,row24,row23,row22,row21,row20,row19,row18,row17,row16,row15,row14,row13,row12,row11,row10,row9,row8,row7,row6,row5,row4,row3,row2,row1,row0]
    return TempList


def Minecon(C,D):
    A = random.choice(BlocksList)
    B = random.choice(BlocksList)
    row0 = [A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row1 = [A,B,B,B,B,B,A,A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row2 = [A,B,A,B,A,B,A,A,B,B,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row3 = [A,B,A,B,A,B,A,A,B,A,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row4 = [A,B,A,A,A,B,A,A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row5 = [A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,B,B,A,A,B,B,B,A,A,A,A,A]
    row6 = [A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,B,B,B,A,A,B,B,B,A,A,A,A,A]
    row7 = [A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row8 = [A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,B,A,A,A,A,A,A,A,A]
    row9 = [A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,B,A,A,A,A,A,A,A,A]
    row10 =[A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row11 =[A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,A,A,A,B,A,A,A,A,A,A]
    row12 =[A,B,B,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,B,B,B,B,A,A,A,A,A,A]
    row13 =[A,B,A,B,B,A,A,A,A,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row14 =[A,B,A,A,B,A,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row15 =[A,A,A,A,A,A,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row16 =[A,B,B,B,B,A,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row17 =[A,B,A,A,A,A,A,A,A,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row18 =[A,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row19 =[A,B,A,A,A,A,A,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,D,A,A,A,D,A,A]
    row20 =[A,B,B,B,B,A,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,D,A,D,A,A,A]
    row21 =[A,A,A,A,A,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,D,A,A,A,A]
    row22 =[A,B,B,B,B,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,C,C,C,C,A,A]
    row23 =[A,B,A,A,A,A,A,A,A,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A,C,C,C,C,A,A]
    row24 =[A,B,A,A,A,A,A,A,A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,C,C,C,C,A,A]
    row25= [A,B,B,B,B,A,A,A,A,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row26= [A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row27= [A,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row28 =[A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row29 =[A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row30 =[A,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    List = [row30,row29,row28,row27,row26,row25,row24,row23,row22,row21,row20,row19,row18,row17,row16,row15,row14,row13,row12,row11,row10,row9,row8,row7,row6,row5,row4,row3,row2,row1,row0]
    return List

def MineconWool(C,D):
    B = (random.choice(WoolList))
    A = (random.choice(WoolList))
    row0 = [A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row1 = [A,B,B,B,B,B,A,A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row2 = [A,B,A,B,A,B,A,A,B,B,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row3 = [A,B,A,B,A,B,A,A,B,A,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row4 = [A,B,A,A,A,B,A,A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row5 = [A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,B,B,A,A,B,B,B,A,A,A,A,A]
    row6 = [A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,B,B,B,A,A,B,B,B,A,A,A,A,A]
    row7 = [A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row8 = [A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,B,A,A,A,A,A,A,A,A]
    row9 = [A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,B,A,A,A,A,A,A,A,A]
    row10 =[A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row11 =[A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,A,A,A,B,A,A,A,A,A,A]
    row12 =[A,B,B,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,B,B,B,B,A,A,A,A,A,A]
    row13 =[A,B,A,B,B,A,A,A,A,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row14 =[A,B,A,A,B,A,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row15 =[A,A,A,A,A,A,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row16 =[A,B,B,B,B,A,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row17 =[A,B,A,A,A,A,A,A,A,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row18 =[A,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row19 =[A,B,A,A,A,A,A,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,D,A,A,A,D,A,A]
    row20 =[A,B,B,B,B,A,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,D,A,D,A,A,A]
    row21 =[A,A,A,A,A,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,D,A,A,A,A]
    row22 =[A,B,B,B,B,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,C,C,C,C,A,A]
    row23 =[A,B,A,A,A,A,A,A,A,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A,C,C,C,C,A,A]
    row24 =[A,B,A,A,A,A,A,A,A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,C,C,C,C,A,A]
    row25= [A,B,B,B,B,A,A,A,A,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row26= [A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row27= [A,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row28 =[A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row29 =[A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row30 =[A,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    List = [row30,row29,row28,row27,row26,row25,row24,row23,row22,row21,row20,row19,row18,row17,row16,row15,row14,row13,row12,row11,row10,row9,row8,row7,row6,row5,row4,row3,row2,row1,row0]
    return List

def RhoneValley():
    A = random.choice(WoolList)
    B = 12#brown
    C = random.choice(WoolList)# yellow
    D = 14#14 PURPLE
    E =5#4 GREEN
    
    row0 = [A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row1 = [A,C,C,C,A,A,C,A,C,A,A,C,A,C,A,A,C,C,C,C,C,A,A,A,A,A,A,A,A,A]
    row2 = [A,C,A,C,A,A,C,A,C,A,A,C,A,C,A,A,C,A,C,A,C,A,A,A,A,A,A,A,A,A]
    row3 = [A,C,C,C,A,A,C,A,C,A,A,A,C,A,A,A,C,A,C,A,C,A,A,A,A,A,A,A,A,A]
    row4 = [A,C,C,A,A,A,A,C,A,A,A,A,C,A,A,A,C,A,A,A,C,A,A,A,A,A,A,A,A,A]
    row5 = [A,C,A,C,A,A,A,C,A,A,A,A,C,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row6 = [A,A,A,A,A,A,A,A,A,A,A,A,C,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row7 = [A,C,A,A,A,A,C,C,C,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row8 = [A,C,A,A,A,A,C,A,C,A,A,A,A,A,A,A,A,A,E,E,A,A,B,A,A,A,A,A,A,A]
    row9 = [A,C,C,C,A,A,C,A,C,A,A,A,A,A,A,A,A,A,A,E,E,B,A,A,A,A,A,A,A,A]
    row10 =[A,C,A,C,A,A,C,C,C,A,A,A,A,A,A,A,A,A,A,A,A,B,A,A,A,A,A,A,A,A]
    row11 =[A,C,A,C,A,A,A,A,A,C,A,C,C,C,C,A,A,D,D,D,D,D,D,D,D,D,A,A,A,A]
    row12 =[A,A,A,A,A,A,A,A,A,A,A,C,A,A,A,A,A,D,D,D,D,D,D,D,D,D,A,A,A,A]
    row13 =[A,C,C,C,A,A,C,A,A,A,A,C,A,A,A,A,A,A,D,D,D,D,D,D,D,A,A,A,A,A]
    row14 =[A,C,A,C,A,A,C,A,A,A,A,C,A,A,A,A,A,A,D,D,D,D,D,D,D,A,A,A,A,A]
    row15 =[A,C,A,C,A,A,C,A,A,A,A,C,A,A,A,A,A,A,A,A,D,D,D,D,A,A,A,A,A,A]
    row16 =[A,C,C,C,A,A,C,A,A,A,A,A,A,A,A,A,A,A,A,A,D,D,D,D,A,A,A,A,A,A]
    row17 =[A,A,A,A,A,A,A,A,A,A,A,A,C,A,A,A,A,A,A,A,A,D,D,A,A,A,A,A,A,A]
    row18 =[A,C,C,C,A,A,C,A,A,A,A,A,C,A,A,A,A,A,A,A,A,D,D,A,A,A,A,A,A,A]
    row19 =[A,C,A,C,A,A,C,A,A,A,A,A,C,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row20 =[A,C,A,C,A,A,C,A,A,A,A,A,C,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row21 =[A,C,A,C,A,A,C,A,A,A,C,C,C,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row22 =[A,C,A,C,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row23 =[A,A,A,A,A,A,C,C,C,A,A,C,C,C,C,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row24 =[A,C,C,C,A,A,C,A,C,A,A,C,A,A,C,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row25= [A,C,A,C,A,A,C,C,C,A,A,C,A,A,C,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row26= [A,C,C,C,A,A,C,A,A,A,A,C,C,C,C,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row27= [A,C,A,A,A,A,C,C,C,A,A,A,A,A,A,C,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row28 =[A,C,C,C,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row29 =[A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row30 =[A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    List = [row30,row29,row28,row27,row26,row25,row24,row23,row22,row21,row20,row19,row18,row17,row16,row15,row14,row13,row12,row11,row10,row9,row8,row7,row6,row5,row4,row3,row2,row1,row0]
    return List

def EagleLabs(C,D):
    A = random.choice(BlocksList)
    B = random.choice(BlocksList)
    row0 = [A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row1 = [A,A,B,B,B,B,A,A,B,A,A,A,A,A,B,B,B,B,A,A,A,A,A,B,B,B,A,A,A,A]
    row2 = [A,A,B,A,A,A,A,A,B,A,A,A,A,A,B,A,A,A,A,A,A,B,B,B,B,B,A,A,A,A]
    row3 = [A,A,B,B,B,A,A,A,B,A,A,A,A,A,B,A,A,A,A,A,A,A,A,A,B,B,A,A,A,A]
    row4 = [A,A,B,A,A,A,A,A,B,A,A,A,A,A,B,A,A,A,A,A,A,B,B,A,B,B,A,B,B,A]
    row5 = [A,A,B,B,B,B,A,A,B,B,B,B,A,A,B,A,A,A,A,A,A,B,B,B,B,B,B,B,B,A]
    row6 = [A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,B,B,B,B,B,B,A,A]
    row7 = [A,A,B,B,B,B,A,A,B,B,B,B,A,A,A,B,A,A,A,A,A,B,B,B,B,B,B,B,A,A]
    row8 = [A,A,B,A,A,B,A,A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,B,B,B,B,B,A,A,A]
    row9 = [A,A,B,A,A,B,A,A,B,A,A,B,A,A,A,B,A,A,A,A,A,A,A,B,B,B,A,A,A,A]
    row10 =[A,A,B,B,B,B,B,A,B,B,B,B,B,A,A,B,A,A,A,A,A,A,A,B,B,A,A,A,A,A]
    row11 =[A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,A,A,A,A,A,A,A,A,B,A,A,A,A,A]
    row12 =[A,A,B,B,B,B,A,A,B,A,A,A,A,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row13 =[A,A,B,A,A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row14 =[A,A,B,A,A,B,A,A,B,A,A,A,A,A,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A]
    row15 =[A,A,B,B,B,B,A,A,B,B,B,B,A,A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A]
    row16 =[A,A,A,A,A,B,A,A,B,A,A,B,A,A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A]
    row17 =[A,A,B,B,B,B,A,A,B,B,B,B,A,A,B,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A]
    row18 =[A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row19 =[A,A,A,B,A,A,A,A,B,B,B,B,A,A,B,B,B,B,B,A,A,A,A,D,A,A,A,D,A,A]
    row20 =[A,A,A,B,A,A,A,A,B,A,A,A,A,A,B,A,B,A,B,A,A,A,A,A,D,A,D,A,A,A]
    row21 =[A,A,A,B,A,A,A,A,B,B,B,B,A,A,B,A,B,A,B,A,A,A,A,A,A,D,A,A,A,A]
    row22 =[A,A,A,B,A,A,A,A,A,A,A,B,A,A,B,A,B,A,B,A,A,A,A,A,C,C,C,C,A,A]
    row23 =[A,A,A,B,A,A,A,A,B,B,B,B,A,A,B,A,A,A,B,A,A,A,A,A,C,C,C,C,A,A]
    row24 =[A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,C,C,C,C,A,A]
    row25= [A,A,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row26= [A,A,B,A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row27= [A,A,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row28 =[A,A,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row29 =[A,A,B,B,B,B,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    row30 =[A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A]
    List = [row30,row29,row28,row27,row26,row25,row24,row23,row22,row21,row20,row19,row18,row17,row16,row15,row14,row13,row12,row11,row10,row9,row8,row7,row6,row5,row4,row3,row2,row1,row0]
    return List

def PrintWall(ImportedList):

    pos = mc.player.getTilePos()
    mc.player.setPos(pos.x,pos.y,pos.z)

    myList = ImportedList
    

    for row in range (0,30):
        for column in range (0,30):
            
            mc.setBlock(pos.x+column,pos.y+row,pos.z-20,myList[row][column])    
            

def PrintWallWool(ImportedList):

    pos = mc.player.getTilePos()
    mc.player.setPos(pos.x,pos.y,pos.z)

    myList = ImportedList
    

    for row in range (0,30):
        for column in range (0,30):
            
            mc.setBlock(pos.x+column,pos.y+row,pos.z-20,35,myList[row][column])    
            
    
#while True:
 #   number = input("type in your pixel art request")
    
  #  if number == 1:
    #    PrintWallWool(StarTrooper((BlocksList,(35,random.choice(BlocksList)))
    #time.sleep(0.5)
    #    mc.postToChat("Hello")
   # elif number == 2:
     #   PrintWallWool(RandomStormy((35,random.choice(BlocksList)),BlocksList))
    #time.sleep(0.5)
    #elif number == 3:
     #   PrintWallWool(RandomWall())
    #time.sleep(0.5)
    #elif number == 4:
     #   PrintWallWool(Minecon(46,103))
    #elif number == 5:
     #   PrintWallWool(RhoneValley())
   # elif number == 6:
    #    PrintWallWool(MineconWool(46,103))
    #elif number == 7:
     #   PrintWall(EagleLabs(46,103))
def PrintHello():
  mc.postToChat("Hello")

def PrintRandomStormy():
  PrintWallWool(RandomStormy((35,random.choice(BlocksList)),BlocksList))

def PrintRandomWall():
  PrintWallWool(RandomWall())
  
def PrintRandomMinecon():
  PrintWallWool(Minecon(46,103))

def PrintRandomRhone():
  PrintWallWool(RhoneValley())

def PrintMineConWool():
  PrintWallWool(MineconWool(46,103))

def PrintEagleLabs():
  PrintWall(EagleLabs(46,103))
  
app = App()
buttonTNT = PushButton(app,dropTNT,text="TNT")
buttonGLASS = PushButton(app,dropGlass,text="GLASS")
buttonWOOL = PushButton(app,dropWOOL,text="Random WOOL")
buttonSayHello = PushButton(app,PrintHello,text="Say Hello")
buttonRandomStormy = PushButton(app,PrintRandomStormy,text="Print Random Stormy")
buttonRandomWall = PushButton(app,PrintRandomWall,text="Print Random Wall")
buttonRandomMinecon = PushButton(app,PrintRandomMinecon,text="Print Random Minecon")
buttonRandomRhone = PushButton(app,PrintRandomRhone,text="PrintRandomRhone")
buttonRandomEagleLabs = PushButton(app,PrintMineConWool,text="Print Random Minecon Wool")
buttonRandomStormy = PushButton(app,PrintEagleLabs,text="Print Random PrintEagleLabs")

app.display()
