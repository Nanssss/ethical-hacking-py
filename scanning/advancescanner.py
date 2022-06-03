#!/usr/bin/python3.8

from socket import * #on import tout de la librairie socket, mieux qui import socket car on a pas a specifier les prefixes
import optparse #servira a specifier les options d'aide
from threading import *

def main(): #ici on va appeler les options valables pour l'user
	parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target port>') # c'est ce qui sera afficher si l'user utilise mal le script
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host') #explique la 1ere option -H si l'utilisateur fait -h pour help
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports separated by comma') #explique la 2eme option -p si idem
	(options, args) = parser.parse_args() #analyse les arguments

	tgtHost = options.tgtHost #tgtHost se refere a tgtHost definie avec parser.add_option
	tgtPorts = str(options.tgtPort).split(",") #str() transforme en string et les separe par les ,

	if (tgtHost == None) | (tgtPorts[0] == None) : #si l'user a rien mis dans les parametres
		print(parser.usage)
		exit(0) #quitte le programme car il y a eu une erreur

	#portScan(tgtHost,tgtPorts)
main()
