#!/usr/bin/python

# this version of deadman-sd-micro is for
# connecting the RPi Zero to a
# microUPS from Yang's project
# no deadman signal needed

# 28 Dec 2018 - gswann
# for Pi Zero added
# Auto Shutdown input

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

mySleep = 5
mySleep1 = 1
mySleep2 = 3

# pinDM not really used
# GPIO19 - header pin35 - 3 up on left
pinDM = LED(19)

print("shutdown monitor starting...")
# GPIO 26, header pin 37 - 2 up on left
sdBtn = 26
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
       if debug == 1:
         print (msg.decode('ascii'))
    except:
          if debug == 1:
            print('couldnt connect')
#          time.sleep(10)
#          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


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
    check_call(['sudo', 'killall', 'motion'])
#    check_call(['sudo', 'rmmod', 'bcm2835-v4l2'])
    time.sleep(1)
    print('Shutdown called')
    
    check_call(['sudo', 'poweroff'])
#    check_call(['ls', '-al'])

# if shutdown signal normally low, must have pull_up=False
shutdown_btn = Button(sdBtn, hold_time=1, pull_up=False)
shutdown_btn.when_held = shutdown
ctr = 0

while(1):

    ctr += 1
    if ctr == 10:
      ctr = 0
      checkin()


 #   myState = GPIO.input(pinDM)
 #   GPIO.output(pinDM, not myState)
    pinDM.on()
    if (debug == 1):
           print("tick")
    sleep(mySleep1)
    pinDM.off()
    if (debug == 1):
           print("tock")
    sleep(mySleep2)

