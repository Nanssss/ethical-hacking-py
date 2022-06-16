#!/usr/bin/python3

from socket import * 
import optparse 
from threading import *
from termcolor import cprint

def connScan(tgtHost, tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM) 
		sock.connect((tgtHost,tgtPort))
		cprint('[+]%d/tcp Open' % tgtPort, 'green')
	except:
		cprint('[-] %d/tcp Closed' % tgtPort, 'red')
	finally:
		sock.close() #ferme la connection

def portScan(tgtHost, tgtPorts):
	# 1 : trouve l'IP si on spécifie un nom de domaine, sinon on l'a déjà
	# 2 : si on trouve le nom de domaine de l'IP, on l'affiche, sinon on affiche l'IP
	try: 
		tgtIP = gethostbyname(tgtHost) #si l'user specifie un nom de domaine et pas une IP, on trouve l'IP du domaine grace a la fonction gethostbyname
	except: 
		print('Can\'t resolve target host %s' %tgtHost)

	try:
		tgtName = gethostbyadrr(tgtIP) #fait l'inverse, get le hostname by the ipaddress
		print('[+] Scan results for : ' + tgtName[0])
	except:
		print('[+] Scan results for: ' + tgtIP)
	setdefaulttimeout(2)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort))) #run all ports with a different thread, target = fonction qui va scanner les ports
		t.start()

def main():
	parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target port>') 
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports separated by comma')
	(options, args) = parser.parse_args() #analyse les arguments

	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(",")

	if (tgtHost == None) | (tgtPorts[0] == None) : #si l'user a rien mis dans les parametres
		print(parser.usage)
		exit(0)

	portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
	main()
