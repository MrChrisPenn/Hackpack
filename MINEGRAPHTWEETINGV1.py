"""
Written by @ncscomputing v2 to work  with Pi Sensehat on Pi not web based.
"""
import subprocess

#====twitter info
import sys
from twython import Twython

#blocksList = [1,2,3,4,5,6,7,12,13,14,15,16,17,18,20,21,22,24,35,41,42,43,44,45,46,47,48,49,51,53,54,56,57,58,60,61,62,67,73,78,79,80,81,82,89,95,98,103,246,247,155]

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


api = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

from sense_hat import SenseHat
sense=SenseHat()



SwitchBlocks = False
mc = minecraft.Minecraft.create()
begX,begY,begz = mc.player.getPos()

mc.camera.setFollow()
mc.player.setting("autojump", False)
mc.player.setPos(6, 60, 50)
blockTypeList=[1,2,3,4,5,6,7,8,9,10,11,12]
OtherBlocks = [1,2,3,4,5,6,7,12,13,14,15,16,17,18,20,21,22,24,35,41,42,43,44,45,46,47,48,49,51,53,54,56,57,58,60,61,62,67,73,78,79,80,81,82,89,95,98,103,246,247,155]
DataStreamList = []

DataStreamCount= 0
def FlatMap():
    print("Clearing map.....")
    mc.setBlocks(-128,0,-128,128,64,128,0)
    time.sleep(5)
    mc.setBlocks(-128,0,-128,128,-64,128,3)
    print("map relaid")

def Tweet():
    time.sleep(6)
    msg = "ESA Sense hat Minegraph twitter bot 1.0"+" :)"
    mc.postToChat(msg)
    
    a=subprocess.check_output('./raspi2png -d 3 -p "myscreenshot.png"',shell=True)
    photo = open('/home/pi/raspi2png/myscreenshot.png', 'rb')
    response = api.upload_media(media=photo)
    api.update_status(status = msg, media_ids=[response['media_id']])



def BuildDataBlock():
    temp=int(sense.get_temperature())
    DataStreamList.append(temp)
    orx,ory,orz = mc.player.getPos()
    if SwitchBlocks == True:
        block = random.choice(blockTypeList)
        for i in range (0,temp):
            x,y,z = orx,ory,orz
        #mc.setBlock(x+(i),y-20,z,35,block)
            mc.setBlock(x,y-40,z+i,35,block)
    else:
        block = random.choice(OtherBlocks)
        for i in range (0,temp):
            x,y,z = orx,ory,orz
        #mc.setBlock(x+(i),y-20,z,35,block)
            mc.setBlock(x,y-40,z+i,block)

    
    mc.player.setPos(orx-1,ory,orz)
    #orx,ory,orz = x-1,y,z
    msg = "Temp currently is:",temp 
    print(msg)
    #msg = "Most recent readings:"+str(DataStreamList)
    #mc.postToChat(msg)

def RestartGraph():
    temp=int(sense.get_temperature())
    DataStreamList.append(temp)
    orx,ory,orz = begX,begY,begz
    block = random.choice(blockTypeList)

    for i in range (0,temp):
        x,y,z = orx,ory,orz
        #mc.setBlock(x+(i),y-20,z,35,block)
        mc.setBlock(x,y-40,z+i,35,block)
    mc.player.setPos(orx-1,ory,orz)
    #orx,ory,orz = x-1,y,z
    msg = "Temp currently is:",temp 
    print(msg)
    #msg = "Most recent readings:"+str(DataStreamList)
    #mc.postToChat(msg)



#FlatMap()    
mc.postToChat("Start Graph")
while True:
    
    mc.camera.setFollow()
    BuildDataBlock()
    time.sleep(10)
    DataStreamCount= DataStreamCount+1
    print(DataStreamCount)
    if DataStreamCount == 30:
        #FlatMap()
        msg = "Last 30 temps: ",DataStreamList
        mc.postToChat(msg)
        Tweet()
        time.sleep(300)
        DataStreamCount = 0
        RestartGraph()
        DataStreamList = []
        if SwitchBlocks == True:
            SwitchBlocks = False
        else:
            SwitchBlocks = True
        
        
