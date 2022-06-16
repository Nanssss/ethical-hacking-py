#!/usr/bin/python3

import socket
from termcolor import colored #librairie pour les couleurs

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
socket.setdefaulttimeout(2) 

host = input("[*] Enter the host to scan: ")

def portscanner(port): 
	if not sock.connect_ex((host,port)) :
		print(colored("[--->] Port %d is open" % (port), 'green'))

for port in range(0,65535):
	portscanner(port)
