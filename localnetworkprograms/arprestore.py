#!/usr/bin/python3

import scapy.all as scapy

def get_target_mac(ip):
	arp_request = scapy.ARP(pdst=ip) #on cree un paquet arp avec pour ip de destination l'ip en argument
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #l'adresse sur laquelle tous les appareils ecoutent
	finalpacket = broadcast/arp_request #on concatene les deux
	answer = scapy.srp(finalpacket, timeout=2, verbose=False)[0] #on garde que la 1ere partie de la liste qui>
	mac = answer[0][1].hwsrc
	return(mac)

def restore(destination_IP, source_IP):
        target_mac = get_target_mac(destination_IP)
        source_mac = get_target_mac(source_IP)
        packet = scapy.ARP(op=2, pdst=destination_IP, hwdst=target_mac,psrc=source_IP,hwsrc=source_mac)
        scapy.send(packet, verbose=False)

try:
	router_IP = input("Entrez l'IP du routeur : ")
	tgt_IP = input("Entrez l'IP de la cible : ")
	restore(router_IP,tgt_IP)
	restore(tgt_IP,router_IP)
	print("Parametres restaures a l'origine")
except:
	print("Erreur !")
	exit(0)
