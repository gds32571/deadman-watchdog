#!/usr/bin/python

# 4 Jan 2018
# this version of deadman-sd is for 
# connecting the RPi Zero to a
# UPS3v2 (the new board)

# a deadman is required to signal the UPS controller
# a second deadman is used to blink an LED
# on the UPS controller

# 29 July 2018 - gswann
# deadman.py program to show
# cpu is running

#import pdb

from gpiozero import Button
from gpiozero import LED
from subprocess import check_call
from subprocess import call

from time import sleep
from datetime import datetime

import socket
import time

debug = 1

#mySleep = 5
mySleep1 = 1
mySleep2 = 3


# GPIO19 - header pin 35 - 3 up on left
pinDM = LED(19)
# GPIO23 - header pin 16 - 8 down on right 
pinDM2 = LED(23)
# GPIO 26, header pin 37 - 2 up on left
sdBtn = 26

print("shutdown monitor starting...")

def checkin():
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'ha32163'
    port = 3004

    try:
       s.connect((host, port))

       # Receive no more than 1024 bytes
       s.sendall(b'mysend')
       msg = s.recv(1024)
       s.close()
       print (msg.decode('ascii'))
    except:
          print('couldnt connect')

checkin()

def shutdown():

    outf = open("/home/pi/deadman/sd.log","a")
    call(['uptime'],stdout=outf )
    outf.flush()

    outf.write("Shutdown called at")
    outf.write(time.strftime(" %Y/%m/%d"))
    outf.write(time.strftime(" %H:%M:%S"))
    outf.write("\n")
    outf.flush()
    outf.close()

    time.sleep(2)
    print('Shutdown called')
    check_call(['sudo', 'poweroff'])
#    check_call(['ls', '-al'])

shutdown_btn = Button(sdBtn, hold_time=5, pull_up=True)
shutdown_btn.when_held = shutdown
ctr = 0

while(1):

    ctr += 1
    if ctr == 3:
      ctr = 0
      checkin()


#    myState = GPIO.input(pinDM)
#    GPIO.output(pinDM, not myState)
    pinDM.toggle()

    for x in range(4):
 
      pinDM2.on()
      if (debug == 1):
         print("tick")
      sleep(mySleep1)
      pinDM2.off()
      if (debug == 1):
         print("tock")
      sleep(mySleep2)

