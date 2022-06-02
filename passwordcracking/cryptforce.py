#!usr/bin/python

import crypt

def CrackPass(cryptWord):
	salt = cryptWord[0:2] #les 2 premieres lettres
	dictionnary = open('dictionnary.txt','r')
	for word in dictionnary.readlines():
		word = word.strip('\n')
		cryptPass = crypt.crypt(word, salt)
		if cryptWord == cryptPass:
			print "[+] Found password: " + word
			return

def main():
	passFile = open('passcrypt.txt','r')
	for line in passFile.readlines():
		if ":" in line: #si : est dans la ligne
			user = line.split(':')[0]
			cryptWord = line.split(':')[1].strip(' ').strip('\n')
			print "[*] Cracking password for : " + user
			CrackPass(cryptWord)

main()
