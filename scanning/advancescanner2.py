#!/usr/bin/python

from socket import * #on import tout de la librairie socket, mieux qui import socket car on a pas a specifier les prefixes
import optparse #servira a specifier les options d'aide
from threading import *

def connScan(tgtHost, tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM) #grace au from socket inport * on a pas besoin de mettre socket. comme prefixe a chaque fois
		sock.connect((tgtHost,tgtPort))
		print ' [+]%d/tcp Open' % tgtPort
	except:
		print '[-] %d/tcp Closed' % tgtPort
	finally:
		sock.close() #ferme la connection

def portScan(tgtHost, tgtPorts):
	try: #essaye de faire ce bloc
		tgtIP = gethostbyname(tgtHost) #si l'user specifie un nom de domaine et pas une IP, on trouve l'IP du domaine grace a la fonction gethostbyname
	except: #si le try rencontre une erreur ce bloc sera execute
		print 'Can\'t resolve target host %s' %tgtHost
	
	try:
		tgtName = gethostbyadrr(tgtIP) #fait l'inverse, get le hostname by the ipaddress
		print '[+] Scan results for : ' + tgtName[0]
	except:
		print '[+] Scan results for: ' + tgtIP
	setdefaulttimeout(2)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort))) #run all of ports with a different thread, target = fonction qui va scanner les ports
		t.start() #start le thread je crois, start les ports

def main(): #ici on va appeler les options valables pour l'user
	parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target port>') # c'est ce qui sera afficher si l'user utilise mal le script
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host') #explique la 1ere option -H si l'utilisateur fait -h pour help
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports separated by comma') #explique la 2eme option -p si idem
	(options, args) = parser.parse_args() #analyse les arguments
	
	tgtHost = options.tgtHost #tgtHost se refere a tgtHost definie avec parser.add_option
	tgtPorts = str(options.tgtPort).split(",") #str() transforme en string et les separe par les ,

	if (tgtHost == None) | (tgtPorts[0] == None) : #si l'user a rien mis dans les parametres
		print parser.usage
		exit(0) #quitte le programme car il y a eu une erreur
	
	portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
	main()
