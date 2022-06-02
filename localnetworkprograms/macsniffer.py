#!/usr/bin/python3

from termcolor import colored
import socket
from struct import *


def eth_addr(a):
	b = '{}:{}:{}:{}:{}:{}'.format(format(a[0],'0>2X'), format(a[1],'0>2X'), format(a[2],'0>2X'), format(a[3],'0>2X'), format(a[4],'0>2X'), format(a[5],'0>2X'))
	return b

try:
	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003)) #AF_PACKET sert a manipuler les packets a un niveau protocole, ntohs permet de convertir positive integers en bytes, RAW packets
except:
	print(colored("[!!] Error on creating socket object",'red'))
	exit(0)

while True:
	packet = s.recvfrom(65535) #on revoit les paquets de 65535 ports et on les stocke dans la variable packet
	packet = packet[0] #seule la 1ere partie nous interesse

	eth_length = 14 #nb de bytes du header ethernet
	eth_header = packet[:eth_length] #on garde juste la partie eth et pas le reste

	eth = unpack('!6s6sH', eth_header) #va nous aider a separer nos trucs, voir tableau de bibliotheque struc pour les caracteres, 6 pour une mac, 6 pour l'autre, 2 pour le protocole
	eth_protocol = socket.ntohs(eth[2]) #le 3 element, donc le protocole, voir avec scapy :ls(Ether)
	print("[+] Destination MAC : " + colored(eth_addr(packet[0:6]),'cyan') + " [+] Source MAC : " + colored(eth_addr(packet[6:12]),'yellow') + "[+] Protocol : " + colored(str(eth_protocol),'magenta'))
