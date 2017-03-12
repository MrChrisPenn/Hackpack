import time
"""
Code written by Martin O'Hanlon in the following blog post:
http://www.stuffaboutcode.com/2016/03/microbit-get-data-from-usb.html

adapted by @ncscomputing
"""
import serial
from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block as block
import random
PORT = "/dev/ttyACM0"
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
#read the first line and flush any bad data
s.readline()

def read_microbit_data():
    #read a line from the microbit,
    data = s.readline()
    #split the microbit data
    data_s = data.rstrip().split(" ")
    Message = True if data_s[0] == "On" else False
    return Message


mc = Minecraft.create()
try:
#type your code here============================== 
    while True:
        
        Message = read_microbit_data()
        if Message == True:
            x,y,z = mc.player.getTilePos()
            mc.postToChat("Start Traffic lights")
            time.sleep(1)
            mc.setBlock(x+10, y-1, z, 35,14)#red
            mc.setBlock(x+10, y-2, z, 35,15)#amber
            mc.setBlock(x+10, y-3, z, 35,15)#green
            time.sleep(1)
            mc.setBlock(x+10, y-1, z, 35,15)#black
            mc.setBlock(x+10, y-2, z, 35,4)#amber
            mc.setBlock(x+10, y-3, z, 35,15)#black
            time.sleep(1)
            mc.setBlock(x+10, y-1, z, 35,15)#black
            mc.setBlock(x+10, y-2, z, 35,15)#amber
            mc.setBlock(x+10, y-3, z, 35,5)#green
            time.sleep(1)
#your code stops here 

finally:
 sleep(1)
 s.close()
