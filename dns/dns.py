#!/usr/bin/python3
# Disclaimer: Educational & authorized testing only, see DISCLAIMER.md

from scapy.all import *

def findDNS(p):
	if p.haslayer(DNS): #si le paquet a un layer DNS
		if p.haslayer(IP): #si le paquet a un layer IP
			print(p[IP].src, end=' : ') #la fin de ligne est egale a ca
		print(p[DNS].summary()) #petit resume du paquet dns


sniff(prn=findDNS)
