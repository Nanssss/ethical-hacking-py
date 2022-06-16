#!/usr/bin/python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #c'est l'objet socket, qu'on assigne a la variable sock ; AF_INET represente IPV4 ; SOCK_STREAM on va utiliser des packets TCP pour faire la connection
socket.setdefaulttimeout(2) #on laisse 2 sec pour scanner le port, sinon ca peut etre tres long 

host = input("[*] Enter the host to scan: ")
port = int(input("[*] Enter the port to scan: "))

def portscanner(port): 
	if sock.connect_ex((host,port)) :
		print("Port %d is closed" % (port)) 
	else:
		print("Port %d is open" % (port)) 

portscanner(port) 
