#!/usr/bin/python


#Client

import os
import sys
import thread
import socket
cl=socket.socket(socket.AF_INET , socket.SOCK_STREAM , 0)
#port number = 3333 defined by server
#serv_IP has to be defined here
serv_IP="192.168.1.4"
cl.connect( (serv_IP, 3333) )
while True:
	x=raw_input()
	cl.send(x)
	print '->', cl.recv(1024)
	
cl.close()

