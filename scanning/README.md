# Scanning

## portscan1.py

Essaye tout simplement de se connecter à un port (spécifié en dur dans le code) de l'IP spécifié.
Affiche en sortie si le port est ouvert ou fermé.

## portscan2.py

Idem sauf que le programme prend en paramètre l'IP de la machine cible et le port à portscanner

## portscan3.py

Idem mais scanne tous les ports de 1 à 1000

## advancescanner.py

Juste un test pour optparse

## advancescanner2.py

Utilise optparse pour prendre des arguments en entrée, -H <hostname> et -p <port1,port2...>
Scanne les ports de l'IP/Host spécifié

## retbanner.py

Scanne les ports 1 à 100 d'une IP spécifiée. En plus de la connection au port, on regarde le retour du port, qu'on affiche s'il est ouvert.

## vulnscan.py & vulnbanner.txt

Le fichier prend en entrée un fichier .txt contenant une liste de vulnérabilités connues.
Il scanne ensuite une série d'ips et de ports comme dans retbanner.py, puis si une banner est retournée, il cherche si celle si existe dans le fichier de vulnérabilités connues.
On aura alors trouvé une vulnérabilité.
