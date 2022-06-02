#!usr/bin/python

from termcolor import colored
import hashlib

def tryOpen(wordlist):
	global pass_file #les variables globales peuvent etre utilisees en dehors des fonctions
	try:
		pass_file = open(wordlist, "r")
	except:
		print("[!!] No such file at that path ! ")
		quit()

pass_hash = input("[*] Enter md5 hash value: ")
wordlist = input("[*] Enter the path to the password file: ")
tryOpen(wordlist)

for word in pass_file:
	print(colored("[-] Trying: " + word.strip("\n"), 'red'))
	enc_word = word.encode('utf-8') #bien mettre en utf-8 avant d'utiliser hex.digest()
	md5digest = hashlib.md5(enc_word.strip()).hexdigest()
	#md5digest = hashlib.md5(bytes(word, 'utf-8')).hexdigest() pk ca ca marche pas ici ?

	if md5digest == pass_hash:
		print(colored("[+] Password foucnd: " + word, 'green'))
		exit(0)

print("[!!] Password not in list")
