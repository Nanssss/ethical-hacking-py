#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #c'est l'objet socket, qu'on assigne a la variable sock ; AF_INET represente IPV4 ; SOCK_STREAM on va utiliser des packets TCP pour faire la connection
socket.setdefaulttimeout(2) #on laisse 2 sec pour scanner le port, sinon ca peut etre tres long (marche pas)

host = raw_input("[*] Enter the host to scan: ")
port = int(raw_input("[*] Enter the port to scan: "))

def portscanner(port): #fonction qui va faire le scan
	if sock.connect_ex((host,port)) :
		print "Port %d is closed" % (port) #si erreur le port est ferme, %d est remplace par ce qu'on met a la fin
	else:
		print "Port %d is open" % (port) #si on a pas d'erreur c'est que c'est bon

portscanner(port) #appel de la fonction
