# Bruteforce

L'attaque par bruteforce, ou attaque par force brute, est une méthode de hacking ancienne et simple. Les applications les plus courantes de cette méthodes sont le craquage de mots de passe ou de clés de cryptage. Elle consiste simplement à tester à la suite des combinaisons identifiants/mots de passe jusqu'à trouver la bonne.
Plusieurs approches peuvent être utilisées :

- L'algorithme va tester toutes les combinaisons possibles

La rapidité de l'attaque va donc être dépendante de la puissance de calcul de la machine de l'attaquant, mais surtout de la complexité du mot de passe. C'est pour celà que la majorité des sites web demandent un mot de passe d'au moins 8 caractères, comprenant des majuscules, minuscules, chiffres et caractères spéciaux. Celà augmente grandement le nombre de combinaisons possibles. On peut voir sur le tableau ci-dessous les effets de la longueur et de la complexité d'un mot de passe :

<p align="center">
  <img align="center" src="../ressources/tab_bruteforce.png" width="700" title="Rapidité des attaques par bruteforce selon la complexité du mot de passe" alt="tab_bruteforce">
  </br>
  <t align="center" style="italic">Rapidité des attaques par bruteforce selon la complexité du mot de passe</t>
</p>

- On peut aussi utiliser des dictionnaires de mots de passe

En effet, il est facile de trouver sur internet des dictionnaires des mots de passe les plus utilisés, certains en contiennent des millions. Si votre mot de passe est contenu dans ces dictionnaires, l'attaque peut alors être bien plus rapide.

*Mais alors, quelles sont les mesures à prendre pour se protéger des attaques par bruteforce ?*
1. Tout d'abord, comme nous l'avons vu, choisir un mot de passe long et complexe augmente grandement le nombre de combinaisons possibles.
2. Ensuite, on peut facilement sécuriser le mécanisme d'authentification en le bloquant après X tentatives de connexion infructueuses.
3. L'authentification multifactorielle est aussi utilisée. C'est par exemple lorsqu'on vous demande en plus d'entrer un mot de passe reçu par SMS.

Une attaque par bruteforce est donc facile à mettre en place, mais il est aussi facile de s'en protéger.

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