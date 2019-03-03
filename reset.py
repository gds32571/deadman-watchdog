#!/usr/bin/python

# 21 Feb 2019 - gswann
# used to reset counters in zerowd.py running for a particular
# client host/app being monitored
# use port on command line

import socket
import time
import sys

def usage(myCLP):
   print"Value '" + myCLP + "' not in list"
   print"   use 3001 for rp5"
   print"   use 3002 for sdr"
   print"   use 3004 for zero4"
   print"   use 3005 for sendtoWU"
   print"   use 3010 for test"

def checkin(port):
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'ha32163'
#    port = 3002

    try:
       s.connect((host, port))
       s.settimeout(5.0)

       # Receive no more than 1024 bytes
       s.sendall(b'reset')
       msg = s.recv(1024)
       s.close()
       print (msg.decode('ascii'))
    except:
          print('couldnt connect')
#          time.sleep(10)
#          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) < 2:
   print "no clp"
   usage(' ')
   sys.exit()
   


clp = int(sys.argv[1])

checkin(clp)
