#!/usr/bin/python3.8
# Disclaimer: Educational & authorized testing only, see DISCLAIMER.md

import socket
from termcolor import cprint

def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket() 
		s.connect((ip,port))
		banner = s.recv(1024) #banner est ce qu'on recoit du port, ici 1024 bytes
		return banner
	except:
		return 

def main():
	ip = input("[*] Enter target IP: ")
	for port in range(1,1023):
		banner = retBanner(ip,port) 
		if banner: 
			cprint("[+]" + ip + "/" + str(port) + ": " + banner.decode(), 'green') #il faut .decode car banner est un byte

main()
