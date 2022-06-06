#!/usr/bin/python3.8

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #c'est l'objet socket, qu'on assigne a la variable sock ; AF_INET represente IPV4 ; SOCK_STREAM on va utiliser des packets TCP pour faire la connection


host = "129.187.229.60"
port = 22 # on va essayer de se connecter sur ce port sur la machine host

def portscanner(port): #fonction qui va faire le scan
	if sock.connect_ex((host,port)) : #sock.connect_ex = sock.connect() mais retourne un error indicator s'il y a problème, au lieu d'une exception
		print("Port %d is closed" % (port)) #si erreur le port est ferme, %d est remplace par ce qu'on met a la fin
	else:
		print("Port %d is opened" % (port)) #si on a pas d'erreur c'est que c'est bon

portscanner(port) #appel de la fonction
