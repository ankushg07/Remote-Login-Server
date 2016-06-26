#!/usr/bin/python

#Server

#Connection on TCP Protocol

#Server will receive the command from client and will 
#execute it on its system then will send the output
#to the respective client

import os , commands
import thread
import socket
def func(cl_ob, cl_add):
	while True:
		cmd=cl_ob.recv(100)
		cmd=cmd.strip()
		op=commands.getstatusoutput(cmd)
		if(op[0] == 0):
			cl_ob.send(op[1])
		else:
			cl_ob.send("Invalid command")
		print cl_add, cmd
	cl_ob.close()


def main():
	serv=socket.socket(socket.AF_INET , socket.SOCK_STREAM , 0)
	#port number = 3333
	#ip addr will be dynamically binded
	serv.bind( ("", 3333) )
	serv.listen(5)
	while True:
		cl_ob, cl_add = serv.accept()
		#multi threading for multi client connection
		thread.start_new_thread(func,(cl_ob , cl_add ))

if __name__ == "__main__":
	main()