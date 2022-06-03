#!/usr/bin/python3.8

import socket
import os
import sys #pour check le nb d'arguments specifies dans la commande du programme
from termcolor import cprint

def checkVulns(banner, filename): #fonction qui teste si la banner est presente dans le ficher des banners vulnerables
	f = open(filename, "r") #pour ouvrir un fichier dans python il faut creer une variable, ensuite on fait open(file, "mode"), il y a 3 modes differents, r pour read
	for line in f.readlines(): #fonction qui permet de lire ligne par ligne
		if line.strip("\n") in banner.decode():
			cprint('[+] Server is vulnerable: ' + banner.decode(), 'green') #strip sert a retirer le caractere saut de ligne

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
	if len(sys.argv) == 2: #si ya 2 arguments
		filename = sys.argv[1] #le filename est l'arg 2
		if not os.path.isfile(filename): #si ce fichier n'existe pas ou si c'est pas un fichier
			cprint('[-] File doesnt exist !', 'red')
			exit(0)
		if not os.access(filename, os.R_OK): #si on a pas acces a ce fichier
			cprint('[-] Access denied !', 'red')
			exit(0)
	else: #s'il n'y a pas 2 args
		cprint('[-] Usage: ' + str(sys.argv[0]) + "<vuln filename>", 'yellow') #on affiche comment utiliser le prgrm
		exit(0)

	#si tout est ok
	portlist = [21,22,25,80,110,443,445] #liste de ports
	for x in range(59,61): #scanne les fin d'ip entre (ici, la)
		ip = "129.187.229." + str(x) #les débuts d'ips
		for port in portlist:
			banner = retBanner(ip,port) #on fait comme le programme precedent
			if banner:
				cprint('[+] ' + ip + "/" + str(port) + " : " + banner.decode(), 'yellow')
				checkVulns(banner, filename) #fonction qui va tester si la banner est dans le fichier des banners vulnerables
main()
