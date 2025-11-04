#!usr/bin/python3
# Disclaimer: Educational & authorized testing only, see DISCLAIMER.md

import ftplib
from termcolor import cprint

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous', 'anonymous') #ftp.login('user', 'mdp')
		cprint("[*] " + hostname + " FTP Anonymous Logon Succeeded.", 'green')
		ftp.quit()
		return True
	except Exception: #n'importe quelle erreur pdt la tentative de connection
		cprint('[-] ' + hostname + " FTP Anonymous Logon Failed.", 'red')

host = input("Enter IP Address : ")
anonLogin(host)
