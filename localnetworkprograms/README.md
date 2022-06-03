# Local Network Programs

## macchange.py

Ce programme sert à changer virtuellement notre addresse mac.
Cependant, il ne marche que sur linux car il utilise des commandes linux.

## arpspooferforwarding.py

Ce programme est un arpspoofer. Il se fait passer pour la victime auprès du routeur et inversement.
Il permet donc d'intercepter des packets.
Il faut activer l'ipforwarding si on veut que la victime ait internet.

## arprestore.py

Ce programme sert à restaurer les paramètres d'origine (au niveau des @ mac)

## ararpspooferforwardingmultiple.py

Même chose que arpspooferforwarding.py, mais avec 2 cibles.

## synflood.py

Ce programme est un SYN flood, il sert à faire des attaques DOS (Denial Of Service). On initie à répétition des connexions à la cible sans les fermer. Le but est de saturer le serveur.
En réalité, pour saturer un serveur, il faudrait le faire avec de nombreuses machines.

## macsniffer.py
