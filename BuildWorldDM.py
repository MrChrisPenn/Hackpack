""" Make a Map in Minecraft"""
__author__ = '@damianmooney'
from mcpi import minecraft as minecraft
from mcpi import block as block
import random
 
 
def clearZone( alocx, alocz, blocx, blocz,mc ):
    mc.setBlocks( alocx, 1, alocz, blocx, 128, blocz, block.AIR )
    mc.setBlocks( alocx, -5, alocz, blocx, 0, blocz, block.WATER )
 
#if __name__ == "__main__":
def Build():
    mc = minecraft.Minecraft.create()
    clearZone( -128, -128, 128, 128,mc )
    print('Cleared')
    f = open('world3.txt', 'r')  # open your ascii art text file
    mymap = f.read()
    f.close()
 
    myrows = mymap.split('\n')
 
    print(mymap)
 
    # --start our top corner of world adjust to get 0,0 ok on map
    x = 100
    z = 85
 
    for i in myrows: #for each line in our map
        #print len(i)
        print(i)
        z -=1
        x = 100
        y = 0
        for j in i:  # go through each position on the current line
            x -=1
            if j != " ":  # if the map is not empty blank minecraft then place a grass block 
                position = (x, y, z)
                mc.setBlock(position, block.AIR)
                mc.setBlock(position, block.GRASS)
            elif j != " ":  # place water
                position = (x, y, z)
                mc.setBlock(position, block.AIR )
                mc.setBlock(position, block.WATER )
