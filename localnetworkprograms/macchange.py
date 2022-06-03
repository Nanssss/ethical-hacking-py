#!usr/bin/python3

import subprocess #permet d'executer des commandes systemes et checker leur output
from termcolor import colored

def change_mac_address(interface,mac):
	try:
		subprocess.call(["sudo ip link set " + interface + " down"], shell=True) #execute juste la fonction
		subprocess.call(["sudo macchanger --mac=" + new_mac_address + " " + interface], shell=True,stdout=subprocess.DEVNULL) #on affiche pas la sortie standard
		subprocess.call(["sudo ip link set " + interface + " up"], shell=True) #execute juste la fonction
	except:
		subprocess.call(["sudo ip link set " + interface + " up"], shell=True) #execute juste la fonction


def main():
	interface = str(input("[*] Enter interface to change mac address on: "))
	global new_mac_address
	new_mac_address = input("[*] Enter mac address to change to: ")

	try:
		before_change = subprocess.check_output(["ip addr show " + interface + " | sed -n 2p"], shell=True) #execute la fonction et store l'output dans la variable
		print("before: " + str(before_change))
		change_mac_address(interface,new_mac_address)
		after_change = subprocess.check_output('ip addr show ' + interface + " | sed -n 2p", shell=True)
		print("after: " + str(after_change))
		if before_change == after_change:
			print(colored("[!!] Failed to change mac address to: " + new_mac_address, 'red'))
		else:
			print(colored("[+] Mac address changed to : ", 'green') + colored(new_mac_address, 'blue') + colored(" on interface " + interface, 'green'))
	except:
		print(colored("Exception !!", 'red'))

main()
