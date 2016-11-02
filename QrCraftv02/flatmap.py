import sys
import mcpi.minecraft as minecraft
import mcpi.block as block
import random

# created by http://www.minecraftforum.net/forums/other-platforms/minecraft-pi-edition/1959866-simple-flatmap-script

mc = minecraft.Minecraft.create()



def main():
    mc.setBlocks(-128,0,-128,128,64,128,0)

    blocksList = [1,2,3,4,20,26,89,46]

    block = random.choice(blocksList)

    mc.setBlocks(-128,0,-128,128,-64,128,block)

#main()
