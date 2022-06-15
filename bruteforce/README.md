# Bruteforce

L'attaque par bruteforce, ou attaque par force brute, est une méthode de hacking ancienne et simple. Les applications les plus courantes de cette méthodes sont le craquage de mots de passe ou de clés de cryptage. Elle consiste simplement à tester à la suite des combinaisons identifiants/mots de passe jusqu'à trouver la bonne.
Plusieurs approches peuvent être utilisées :

- L'algorithme va tester toutes les combinaisons possibles
La rapidité de l'attaque va donc être dépendante de la puissance de calcul de la machine de l'attaquant, mais surtout de la complexité du mot de passe. C'est pour celà que la majorité des sites web demandent un mot de passe d'au moins 8 caractères, comprenant des majuscules, minuscules, chiffres et caractères spéciaux. Celà augmente grandement le nombre de combinaisons possibles. On peut voir sur le tableau ci-dessous les effets de la longueur et de la complexité d'un mot de passe :

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Tableau rapidité attaques par bruteforce (source : ionos.fr)"

## gmailbrute.py

Bruteforcer pour gmail en utilisant le serveur smtp. Cependant, au bout d'un certain nombre de tests, le serveur nous bloque.

## websitebruteforcer.py

Programme servant à bruteforce n'importe quelle page de login. Il faut juste adapter les champs en haut du programme pour matcher avec le site voulu. Après, en réalité, les sites nous bloquent après un certain nombre de tentatives.

## directories.py

Bruteforce un site web pour trouver les directories du site auxquels on peut accéder.

## subdomains.PY

Idem que le programme précedent mais va chercher les subdomains.

## falseheader.py

Ce programme sert à modifier nos headers, on peut alors se faire passer pour une autre machine auprès d'un site web.

## baseordigestauth.py

Sert à bruteforce des sites utilisant les méthodes basic ou digest.