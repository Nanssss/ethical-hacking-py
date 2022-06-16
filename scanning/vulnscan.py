#!/usr/bin/python3.8

import socket
import os
import sys 
from termcolor import cprint

portlist = [21,22,25,80,110,443,445,902] #liste de ports
iplist = ["192.168.0.100", "192.168.0.102"]

def checkVulns(banner, filename, ip): #fonction qui teste si la banner est presente dans le ficher des banners vulnerables
	f = open(filename, "r")
	for line in f.readlines():	
		if line.strip("\n") in banner.decode():
			cprint('[+] IP {} is vulnerable: {}'.format(ip, banner.decode()), 'green') 

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return

def main():
	if len(sys.argv) == 2: 
		filename = sys.argv[1] 
		if not os.path.isfile(filename):
			cprint('[-] File doesnt exist !', 'red')
			exit(0)
		if not os.access(filename, os.R_OK): 
			cprint('[-] Access denied !', 'red')
			exit(0)
	else:
		cprint('[-] Usage: ' + str(sys.argv[0]) + "<vuln filename>", 'yellow')
		exit(0)

	#si tout est ok
	for ip in iplist: 
		for port in portlist:
			banner = retBanner(ip, port) 
			if banner:
				cprint('[+] Banner found :' + ip + "/" + str(port) + " : " + banner.decode(), 'yellow')
				checkVulns(banner, filename, ip) #fonction qui va tester si la banner est dans le fichier des banners vulnerables
main()
