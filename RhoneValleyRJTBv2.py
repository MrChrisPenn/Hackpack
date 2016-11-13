

"""
0. Use a Raspberry Pi with Raspian OS
1. Work through the RPI Foundation how to setup a Twitter app tutorial https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/
  
2. Install raspi2png to take screen shots of MCPI (paste this in lx terminal)(taken from Martin O'Hanlon http://www.stuffaboutcode.com/2016/03/raspberry-pi-take-screenshot-of.html)

cd ~
git clone https://github.com/AndrewFromMelbourne/raspi2png


3. Install twython by typing the following into LX terminal:

sudo pip3 install twython

4. Save this script in the Raspi2png folder in the home directory 
4.5 Run this python script in python 3.4
5. Position yourself in minecraft
6. Wait and go to twitter :)
"""
__author__ = '@ncscomputing / @warksraspijam'
from mcpi import minecraft as minecraft
from mcpi import block as block
import time
import random
import subprocess

#====twitter info
import sys
from twython import Twython

blocksList = [1,2,3,4,5,6,7,12,13,14,15,16,17,18,20,21,22,24,35,41,42,43,44,45,46,47,48,49,51,53,54,56,57,58,60,61,62,67,73,78,79,80,81,82,89,95,98,103,246,247,155]

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


api = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

BlocksList = [1,2,3,4,5,7,12,13,14,15,16,17,18,20,21,22,24,41,42,45,46,47,49]
WoolList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


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

def PrintWall(ImportedList):

    pos = mc.player.getTilePos()
    mc.player.setPos(pos.x,pos.y,pos.z)

    myList = ImportedList
    

    for row in range (0,30):
        for column in range (0,30):
            
            mc.setBlock(pos.x+column,pos.y+row,pos.z-20,35,myList[row][column])    
            
def Tweet(recip):
    time.sleep(6)
    msg = "Rhone Valley Raspberry Jam"+" :)"
    mc.postToChat(msg)
    
    a=subprocess.check_output('./raspi2png -d 3 -p "myscreenshot.png"',shell=True)
    photo = open('/home/pi/raspi2png/myscreenshot.png', 'rb')
    response = api.upload_media(media=photo)
    api.update_status(status = msg, media_ids=[response['media_id']])

#    time.sleep(600)

mc = minecraft.Minecraft.create()


def Main(recip):# 57 47 14 46 103 Rjam
    
    PrintWall(RhoneValley())
    time.sleep(5)
    Tweet(recip)

def WoolMain(recip):# 57 47 14 46 103 Rjam
    
    PrintWall(MineconWool(46,103))
    time.sleep(5)
    Tweet(recip)
count = 0
while True:
    #WoolMain("@warksraspijam")
    #time.sleep(60)
    Main("@tyrower")
    time.sleep(20)


