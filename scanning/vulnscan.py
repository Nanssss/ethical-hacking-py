#!/usr/bin/python

import socket
import os
import sys #check le nb d'arguments specifies dans la commande du programme


def checkVulns(banner, filename): #fonction qui teste si la banner est presente dans le ficher des banners vulnerables
	f = open(filename, "r") #pour ouvrir un fichier dans python il faut creer une variable, ensuite on fait open(file, "mode"), il y a 3 modes differents, r pour read
	for line in f.readlines(): #fonction qui permet de lire ligne par ligne
		if line.strip("\n") in banner:
			print '[+] Server is vulnerable: ' + banner.strip("\n") #strip sert a retirer le caractere saut de ligne

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
			print '[-] File doesnt exist !'
			exit(0)
		if not os.access(filename, os.R_OK): #si on a pas acces a ce fichier
			print '[-] Access denied !'
			exit(0)
	else: #s'il n'y a pas 2 args
		print '[-] Usage: ' + str(sys.argv[0]) + "<vuln filename>" #on affiche comment utiliser le prgrm
		exit(0)

	#si tout est ok
	portlist = [21,22,25,80,110,443,445] #liste de ports
	for x in range(44,46): #scanne les fin d'ip entre (ici, la)
		ip = "192.168.1." + str(x) #les ip
		for port in portlist:
			banner = retBanner(ip,port) #on fait comme le programme precedent
			if banner:
				print '[+] ' + ip + "/" + str(port) + " : " + banner
				checkVulns(banner, filename) #fonction qui va tester si la banner est dans le fichier des banners vulnerables
main()
