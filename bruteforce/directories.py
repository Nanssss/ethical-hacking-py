#!/usr/bin/python3

import requests


def request(url):
	try:
		return requests.get(url)
	except requests.exceptions.ConnectionError:
		pass #on a pas reussi a se connecter dc la page existe pas


target_url = input("[*] Enter target URL with http\(s\): ")

file = open("common.txt", "r")
for line in file:
	word = line.strip()
	full_url = target_url + "/" + word
	response = request(full_url)
	if response: #si request ne retourne rien, donc si ca a pas marche
		print("[+] Discovered directory at this link : " + full_url)
