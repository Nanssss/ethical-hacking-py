#!usr/bin/python

import ftplib

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous', 'anonymous') #ftp.login('user', 'mdp')
		print "[*] " + hostname + " FTP Anonymous Logon Succeeded."
		ftp.quit()
		return True
	except Exception, e: #n'importe quelle erreur pdt la tentative de connection
		print '[-] ' + hostname + " FTP Anonymous Logon Failed."

host = raw_input("Enter IP Address : ")
anonLogin(host)
