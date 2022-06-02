#!/usr/bin/python3

import requests


def request(url):
	try:
		return requests.get(url)
	except requests.exceptions.ConnectionError:
		pass #on a pas reussi a se connecter dc la page existe pas


target_url = input("[*] Enter target URL: ")

file = open("common.txt", "r")
for line in file:
	word = line.strip()
	full_url = "http://" + word + "." + target_url #pour plus tard rajouter https
	response = request(full_url)
	if response: #si request ne retourne rien, donc si ca a pas marche
		print("[+] Discovered subdomain at this link : " + full_url)
