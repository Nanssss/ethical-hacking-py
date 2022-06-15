# Local Network Programs

## macchange.py

**Ne marche que sur linux avec macchanger installé car il utilise cette commande.**

Ce programme sert à changer virtuellement notre addresse mac. Celà permet de se faire passer pour une autre machine. Par exemple, certains systèmes bannissent des machines en utilisant leur addresse mac, ce programme peut permettre de bypasser ce bannissement.

**Utilisation :**
`sudo python3 arpspooferforwarding.py`

Il va vous demander l'interface sur laquelle vous voulez changer votre mac, j'imagine que ce sera **wlan0** ou **eth0**, puis entrez l'@ mac que vous voulez avoir.

## arpspooferforwarding.py

Ce programme est un arpspoofer. Il sert à se faire passer pour le routeur auprès de la victime et inversement. Il est donc un outil indispensable pour mener des attaques MITM (Man In The Middle). Une fois l'arpspoofer activé, tous les paquets échangés entre la victime et le routeur passent par la machine de l'attaquant. L'arp spoofing est donc la base pour le sniffing de paquets ou le DNS Spoofing.

Il faut activer l'ipforwarding si on veut que la victime ait internet, pour ce faire, il y a le programme ipforward.sh.

`sudo ./ipforward.sh 1` pour activer l'ip forwarding et `sudo ./ipforward.sh 0` pour le désactiver.


**Utilisation :**

`sudo python3 arpspooferforwarding.py` 

Il va vous demander l'IP du routeur et l'IP de la victime. Une fois celà fait, l'attaque sera en cours.

## synflood.py

Ce programme est un SYN flooder, il sert à faire des attaques DOS (Denial Of Service). On initie à répétition des connexions à la cible sans les fermer. Le but est de saturer un serveur ou une machine.
En réalité, pour saturer un serveur, il faudrait le faire avec de nombreuses machines.

**Utilisation :**

`sudo python3 synflood.py` 

Il va ensuite vous demander la fake IP à utiliser pour envoyer les paquets, le port source à utiliser, l'IP de la cible, et le contenu du paquet TCP (vous pouvez mettre n'importe quoi).

## macsniffer.py

**A utiliser ne parallèle de l'arpspoofer, ou à tester localement**

Ce programme nous sert à sniffer les paquets passant sur le réseau, et afficher les mac des machines communiquantes.

**Utilisation :**

`sudo python3 macsniffer.py`

Simplement exécuter le programme.

## ftpsniff.py

**A utiliser ne parallèle de l'arpspoofer, ou à tester localement**

Ce programme sert à sniffer la connexion à un serveur ftp. Lorsqu'il détecte une connexion, il affiche l'user et le mdp. Cela permet donc ensuite d'accéder à toutes les données du serveur ftp en s'y connectant.

**Utilisation :**

`sudo python3 ftpsniff.py -i [interface]`

Une fois des identifiants ftp trouvés il les affichera. Pour le test, j'ai utilisé la machine virtuelle metasploitable qui fait tourner un serveur ftp non sécurisé.

## httpsniffer.py

**A utiliser ne parallèle de l'arpspoofer, ou à tester localement**

Ce programme sert à sniffer les paquets HTTP, puisque ceux-ci ne sont pas cryptés. Il enregistre les paquets trouvés dans un log, et affiche les user et password trouvés s'ils sont dans le pattern écrit dans le programme.
On remarque alors le manque de sécurité du protocole HTTP, il faut bien vérifier qu'on est en HTTPS avant de saisir des identifiants ou de faire des opérations bancaires par exemple.

**Utilisation :**

`sudo python3 httpsniffer.py` 

Il va ensuite vous demander l'interface sur laquelle sniffer les paquets HTTP.