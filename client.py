#!/usr/bin/python


#Client

import os
import sys
import thread
import socket
cl=socket.socket(socket.AF_INET , socket.SOCK_STREAM , 0)
#port number = 3333 defined by server
#ip addr will be dynamically binded
cl.connect( ("", 3333) )
while True:
	x=raw_input()
	cl.send(x)
	print '->', cl.recv(1024)
	
cl.close()

