# Password Cracking

Divers programmes de cracking de mots de passe cryptés.

## hasher.py

Demo de hashage :
Prend une chaine de caractère en entrée, et la hash en md5, sha 1, 222, 256, 512, puis affiche le string résultant.

Ces protocoles sont des algorithmes de hashage. Ils sont très utilisés dans d'innombrables applications de nos jours.

- Ils sont utilisés pour générer des clés (ou empreintes) **uniques** protégeant des données. Il peuvent par exemple permettre de crypter un mot de passe ou de controler l'intégrité d'un fichier.
- Chaque protocole a une taille d'empreinte différente : 128 bits pour md5, 160 bits pour sha1, 224 bits pour sha224, 256 bits pour sha256, 512 bits pour sha512. Evidemment, plus l'empreinte est longue, plus l'algorithme est complexe.
- L'opération est irréversible, il est donc impossible de retrouver le mot de passe à partir du hash

## sha1brute.py

Prend un sha1 en entrée, puis compare sa valeur avec celle d'un dictionnaire d'un mot de passe (ici fourni par url) qu'on hashe.
Si on trouve une valeur de sha1 égale, alors on aura trouvé le mot de passe.

## md5brute.py

Idem que le bruteforce sha1, mais cette fois-ci avec du md5.

## cryptforce.py

Ici, on bruteforce un cryptage de type salt.
C'est un cryptage qui rajoute un préfixe/suffixe (à partir du salt) devant/après le mot de passe, puis le hashe. Le résultat est alors totalement différent du hashage
du mot de passe original. Il faut donc connaitre le salt pour pouvoir retrouver le mdp.

Ici, le programme prend le mdp hashé qu'on recherche, puis le compare avec un dictionnaire de mdp qu'on hashe en supposant que le hash est les 2 premières lettres
