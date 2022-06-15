#!/usr/bin/python3

import requests
from termcolor import cprint


def request(url):
	try:
		return requests.get(url)
	except requests.exceptions.ConnectionError:
		pass #on a pas reussi a se connecter dc la page existe pas


target_url = input("[*] Enter target URL with http(s): ")
passwdfile =input("[*] Enter the path to the file containing directories to be tested: ")
file = open(passwdfile, "r")

file = open(passwdfile, "r")
for line in file:
	word = line.strip()
	full_url = target_url + "/" + word
	response = request(full_url)
	if response: #si request ne retourne rien, donc si ca n'a pas marche
		cprint("[+] Discovered directory at this link : " + full_url, 'green')
