#!/usr/bin/python
# Echo server program

# gswann Dec 2018
# first in Pace, then rewrittten
# as generic module similar to gtserver.py
# on amd1

# do this to install mosquitto on Pi Zero computer
# sudo apt install mosquitto mosquitto-clients


#import pdb
import socket
import paho.mqtt.publish as publish
import sys

#print str(sys.argv)
#print sys.argv[1]



def usage(myCLP):
   print"Value '" + myCLP + "' not in list"
   print"   use 1 for rp5"
   print"   use 2 for sdr"
   print"   use 3 for zero4"

if len(sys.argv) < 2:
   print "no clp"
   usage(' ')
   sys.exit()

#pdb.set_trace()
#print str(sys.argv)

clp = sys.argv[1]
arrDatatype = ['1','2','3']

try:
   datatype = arrDatatype.index(clp)
except:
   usage(clp)
   sys.exit()

arrPort = [3001,3002,3004]
PORT = arrPort[datatype]

arrName = ["rp5","sdr","zero4"]
srvName = arrName[datatype]
print "listening for " + srvName + " on port " + str(PORT)

hassHost = "192.168.2.6"
ctr = 0
HOST = ''                # Symbolic name meaning all available interfaces
#PORT = 3004              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.settimeout(75.0)
s.listen(2)
while True:
 try:
  conn, addr = s.accept()
  myStr = 'Connection ' + str(ctr) + ' from ' + str(addr) + '(' + srvName + ')'
  print myStr
  while True:
    data = conn.recv(1024)
    conn.sendall('reply ' +   str(ctr)  )
    ctr += 1

    try:
      publish.single(srvName + "/apprunning" , "yes" , hostname=hassHost, auth = {'username':"hassuser", 'password':"hasspw"})
    except:
      print("Couldn't publish " + srvName + "/apprunning")
    break

 except KeyboardInterrupt:
    print('keyboard interrupt %s')
    exit()
 except:
    print('timeout ' + srvName )
    try:
      publish.single(srvName + "/apprunning" , "no" , hostname=hassHost, auth = {'username':"hassuser", 'password':"hasspw"})
    except:
      print("Couldn't publish " + srvName + "/apprunning")

conn.close()
              
                                                                               