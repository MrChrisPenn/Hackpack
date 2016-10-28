#QRCraft v0.1

"""
This code is derived from an article by Les Pounder which can be accessed via
https://drive.google.com/file/d/0BwN8u0C7hZzvVGJQZzEyakxGUEU/view

I(@ncscomputing / @warksraspijam ) have repurposed it to start interacting with
Minecraft Pi

"""

# import modules
import RainbowRoadRemix as rrr
import hackoween as Hw
import flatmap as fm
import mcpi.minecraft as minecraft
from sys import argv
import zbar
#Variable
global code

mc = minecraft.Minecraft.create()

mc.postToChat("Welcome to QRcraft V0.2")


#Functions
def scanner():
    global code
    proc = zbar.Processor()
    proc.parse_config('enable')
    device = '/dev/video0'
    if len(argv) > 1:
        device = argv[1]
    proc.init(device)
    proc.visible = True
    proc.process_one()
    proc.visible = False
    for symbol in proc.results:
        code = symbol.data

#Events this is handled via QR codes.
def QrCraftLogic():
        global code
        if code == "Hello":
            mc.postToChat("Hello from QR code")
            #code = ""
        elif code == "Flatten":
            #mc.postToChat("About to flatten world come back in 3 minutes :)")
            print "Flatten"
            fm.main()
            #code = ""
        elif code == "Hackoween":
            #mc.postToChat("About to flatten world come back in 3 minutes :)")
            print "Hackoween"  
            Hw.main()
            #code = ""
        elif code == "Rainbow Road":
            print "Rainbow Road"
            rrr.main()
                
scanner()
while True:
    QrCraftLogic()
    code = ""
    scanner()
    
    #fm.main()
    
    #scanner()
    
