#!/usr/bin/python

import socket
from termcolor import colored #librairie pour les couleurs

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #c'est l'objet socket, qu'on assigne a la variable sock ; AF_INET represente IPV4 ; SOCK_STREAM on va utiliser des packets TCP pour faire la connection
socket.setdefaulttimeout(2) #on laisse 2 sec pour scanner le port, sinon ca peut etre tres long (marche pas)

host = input("[*] Enter the host to scan: ")

def portscanner(port): #fonction qui va faire le scan
	if sock.connect_ex((host,port)) :
		print (colored("[*] Port %d is closed" % (port), 'red')) #si erreur le port est ferme, %d est remplace par ce qu'on met a la fin
	else:
		print (colored("[--->] Port %d is open" % (port), 'green') ) #si on a pas d'erreur c'est que c'est bon

for port in range(1,1000):
	portscanner(port)
