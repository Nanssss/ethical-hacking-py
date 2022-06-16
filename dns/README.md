# DNS Spoofer

## dns.py

**A utiliser en parallèle de l'arpspoofer, ou à tester localement**

Sniffe les paquets DNS et affiche des informations dessus.

**Utilisation :**

    sudo python3 dns.py

## dnsspoof.py

**A utiliser en parallèle de l'arpspoofer, ou à tester localement**

Crée un DNS Spoofer. Un DNS Spoofer permet d'intercepter les paquets DNS, et de les modifier afin de rediriger vers l'adresse voulue, par exemple la notre, sur laquelle on peut faire tourner un serveur apache qui imite une page connue mais non sécurisée. On peut donc par exemple obtenir des mots de passe ou des identifiants bancaires en imitant une page de login ou un site d'achat.

**Ce programme a un problème. Par exemple, j'ai choisi que lorsque la cible va sur le site du cnrs, le programme la redirige vers ma machine faisant tourner apache 2, mais lorsque la cible essaye de se connecter au site du CNRS, il y a une erreur de connexion. J'imagine que le problème vient de mauvaises règles IPTables, mais malgré de nombreuses tentatives, je n'ai pas réussi à trouver les bonnes.**

**Utilisation :**

**Avant de lancer le programme, choisir vers quelle IP on veut rediriger à la ligne 23 dans le champ "rdata". De plus, j'ai choisi de rediriger la cible si elle va sur le site du cnrs, mais on peut changer cela ligne 21.**

    sudo python3 dnsspoofer.py

## dnspoofsummary.py

Idem que le précédent mais print le summary du paquet.

**Utilisation :**

    sudo python3 dnsspoofersummary.py