#!usr/bin/python

from urllib.request import urlopen #la seule fonciton dont on a besoin dans cette librairie
import hashlib
from termcolor import colored

sha1hash = input("[*] Enter Sha1 hash value: ")

passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')
#on met le lien dans la fonction url open, le lien doit contenir seulement les mdp donc sur guithub on clique sur raw

for password in passlist.split('\n'): #on les separe par les \n
	hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest() #bien preciser bytes pour le type/encodage
	if hashguess == sha1hash:
		print(colored("[+] The password is : " + str(password), 'green'))
		quit()
	else:
		print(colored("[-] Password guess " + str(password) + " does not match, trying next...", 'red'))
print("Password not in passwordlist")
