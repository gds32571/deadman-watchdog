#!/usr/bin/python

import socket
import time
import sys

if len(sys.argv) < 2:
   print "no clp"
   sys.exit()


def checkin(port):
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'ha32163'
#    port = 3002

    try:
       s.connect((host, port))
       s.settimeout(5.0)

       # Receive no more than 1024 bytes
       s.sendall(b'mysend')
       msg = s.recv(1024)
       s.close()
       print (msg.decode('ascii'))
    except:
          print('couldnt connect')
#          time.sleep(10)
#          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clp = int(sys.argv[1])

checkin(clp)
