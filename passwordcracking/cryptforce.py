#!usr/bin/python3
# Disclaimer: Educational & authorized testing only, see DISCLAIMER.md

import crypt
from termcolor import cprint

def CrackPass(cryptWord):
	salt = cryptWord[0:2] # le salt est ici 2 premieres lettres
	dictionnary = open('dictionnary.txt','r')
	for word in dictionnary.readlines():
		word = word.strip('\n')
		cryptPass = crypt.crypt(word, salt)
		# compare la valeur du mdp hashé avec celle du dictionnaire hashé avec le salt, si on a le même résultat alors on a trouvé le mdp
		if cryptWord == cryptPass:
			cprint("[+] Found password: " + word + '\n', 'green')
			exit(0)

def main():
	passFile = open('passcrypt.txt','r')
	for line in passFile.readlines():
		if ":" in line: #si : est dans la ligne
			user = line.split(':')[0]
			cryptWord = line.split(':')[1].strip(' ').strip('\n')
			print("[*] Cracking password for : " + user)
			# prend en entrée le mot de passe hashé qu'on va bruteforcer
			CrackPass(cryptWord)
			cprint('[-] Not found', 'red')

main()
