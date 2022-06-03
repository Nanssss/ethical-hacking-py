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

Ce programme nous sert à sniffer les paquets passant sur le réseau, et afficher les mac des machines communiquant.
** **Il faut l'utiliser ne parallèle de l'arpspoofer.** **

## ftpsniff.py

Ce programme sert à sniffer la connexion à un serveur ftp. Lorsqu'il détecte une connexion, il afficher l'user et le mdp.
** **Il faut l'utiliser ne parallèle de l'arpspoofer.** **

## httpsniffer.py

Ce programme sert à sniffer les paquets HTTP, puisque ceux-ci ne sont pas cryptés. Il enregistre les paquets trouvés dans un log, et affiche les user et password trouvés
s'ils sont dans le pattern écrit dans le programme.
** **Il faut l'utiliser ne parallèle de l'arpspoofer.** **
