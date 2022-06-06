#!/usr/bin/python3.8

import socket
from termcolor import cprint

def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket() #ici pas important de preciser si c'est ipv4 ou TCP
		s.connect((ip,port))
		banner = s.recv(1024) #banner est ce qu'on recoit du port, ici 1024 bytes
		return banner
	except:
		return #on fait rien on quitte juste la fonction si ca marche pas

def main():
	ip = input("[*] Enter target IP: ")
	for port in range(1,100):
		banner = retBanner(ip,port) #variable qui stocke les resultats des ports nous renvoyant une banner
		if banner: #si la banner existe
			cprint("[+]" + ip + "/" + str(port) + ": " + banner.decode(), 'green') #il faut .decode car banner est un byte

main()
