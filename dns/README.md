# DNS Spoofer

## dns.py

Sniffe les paquets DNS et affiche des informations dessus.
Pour l'utiliser sur une victime, il faut l'utiliser en parallèle le l'arp spoofer.

## dnsspoof.py

Crée un DNS Spoofer, ce programme permet d'intercepter les paquets DNS, et de les modifier afin de rediriger vers l'adresse voulue (par exemple la notre, sur laquelle on peut faire tourner un serveur apache qui imite une page connue).
** A utiliser en parallèle de l'arp spoofer **

## dnspoofsummary.py

Idem que le précédent mais print le summary du paquet.