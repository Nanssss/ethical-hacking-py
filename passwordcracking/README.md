# Password Cracking

Divers programmes de cracking de mots de passe cryptés en md5 et sha.

Ces protocoles sont des algorithmes de hashage. Ils sont très utilisés dans d'innombrables applications de nos jours.

- Ils sont utilisés pour générer des clés (ou empreintes) **uniques** protégeant des données. Il peuvent par exemple permettre de crypter un mot de passe ou de controler l'intégrité d'un fichier.
- Chaque protocole a une taille d'empreinte différente : 128 bits pour md5, 160 bits pour sha1, 224 bits pour sha224, 256 bits pour sha256, 512 bits pour sha512. Les algorithme ont ainsi évolué en complexité et en longueur d'empreinte au fil du temps. Aujourd'hui par exemple, le md5 est totalement obsolète à cause de l'augmentation de la puissance de calcul des ordinateurs.
- L'opération est irréversible, il est donc impossible de retrouver le mot de passe à partir du hash.

## hasher.py

Demo de hashage :
Prend une chaine de caractère en entrée, et la hash en md5, sha 1, 222, 256, 512, puis affiche le string résultant.

**Utilisation :**

`python3 hasher.py`

Il va ensuite demander une chaine de caractères à hasher. Vous pouvez par exemple entrer "**superman**", qui vous donnera les hashs suivants :

**md5 : `84d961568a65073a3bcf0eb216b2a576`**

**sha1 : `18c28604dd31094a8d69dae60f1bcd347f1afc5a`**

## md5brute.py

L'opération de hashage est irréversible, pour retrouver un mot de passe, on va donc procéder à l'envers. On va en fait tester avec différents mots de passe qu'on va crypter, si le hash obtenu à la fin est le même, on aura alors retrouvé le mot de passe (l'empreinte étant unique).

Prend un hash md5 en entrée, puis compare sa valeur avec celle d'un dictionnaire de mots de passe, qu'on hashe.

Si on trouve une valeur de sha1 égale, alors on aura trouvé le mot de passe.

**Utilisation :**

`python3 md5brute.py`

Il va ensuite vous demander le hash à cracker et le path du dictionnaire/fichier à utiliser. Vous pouvez voir que si vous utilisez le hash md5 de "superman" (en gras au-dessus) et le dictionnaire **passwordcracking/dictionnary.py**, il va bien trouver que "superman" était le mot de passe originel (vu qu'il est contenu dans le dictionnaire).

## sha1brute.py

Même fonctionnement que le programme précedent, seulement, cette fois-ci, le dictionnaire est donné par url.

**Utilisation :**

`python3 sha1brute.py`

Il va ensuite vous demander le hash à cracker. Si vous utilisez le hash sha1 de "superman" (en gras au-dessus), il va bien trouver que "superman" était le mot de passe originel (vu qu'il est contenu dans le dictionnaire).

On pourrait procéder de même pour les autres cryptages sha224, 256 etc.

## cryptforce.py

Ici, on bruteforce un cryptage de type salt.
C'est un cryptage qui rajoute un préfixe/suffixe (à partir du salt) devant/après le mot de passe, puis le hashe. Le résultat est alors totalement différent du hashage du mot de passe originel. Il faut donc connaitre le salt pour pouvoir retrouver le mot de passe. C'est un bon outil pour se protéger des attaques par bruteforce, dictionnaire ou rainbow-tables.

Ici, le programme prend le mot de passe hashé qu'on recherche, puis le compare avec hash des mots de passe d'un dictionnaire auxquels on aura ajouté le salt (ici constitué des 2 premières lettres du mot de passe).

**Utilisation :**

`python3 cryptforce.py`

Il suffit d'exécuter le programme. Le programme va aller chercher des combinaisons user:mdp(hashé) à cracker dans le fichier passcrypt.txt, qu'il va comparer avec les hash des mdp contenus dans dictionnary.txt en ajoutant le salt (pour obtenir le hash de superman avec le salt, j'ai simplement exécuté `crypt.crypt("superman", "su")` dans python)