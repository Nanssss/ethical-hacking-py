#!/usr/bin/python3

import requests
from termcolor import cprint


def request(url):
	try:
		return requests.get(url)
	except requests.exceptions.ConnectionError:
		pass #on a pas reussi a se connecter dc la page existe pas


target_url = input("[*] Enter target URL: ")
passwdfile =input("[*] Enter the path to the file containing subdomains to be tested: ")
file = open(passwdfile, "r")
url = target_url.split("://")

file = open(passwdfile, "r")
for line in file:
	word = line.strip()
	full_url = url[0] + "://" + word + "." + url[1]
	try:
		response = request(full_url)
		if response: #si request ne retourne rien ça a pas marché
			cprint("[+] Discovered subdomain at this link : " + full_url, 'green')
	except KeyboardInterrupt:
		break
	except:
		pass
