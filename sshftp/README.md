# SSH & FTP attacks

Les protocoles SSH et FTP sont des protocoles très utilisés. De plus, ils sont très intéressants pour un attaquant puisque le SSH permet d'avoir le contrôle de la machine cible, et le FTP donne accès à des informations internes.

## sshlogin.py

Automatise la connexion à un shell ssh grâce à pexpect, puis run une commande et print le retour.

**Utilisation :**

`python3 sshlogin.py`

Ensuite, le programme va vous demander l'IP de la machine à laquelle se connecter, ainsi que l'user et le mdp ssh.

## sshbruteforce.py & passwords.txt

Fait la même chose que sshlogin.py mais bruteforce à l'aide d'une liste de mdp.

**Utilisation :**

`python3 sshbruteforce.py`

Il va vous demander l'IP de la cible et l'user pour le SSH. Pour ce test, j'ai utilisé metasploitable.

## anonloginftp.py

Essaye de se connecter en ftp en anonyme à l'hôte spécifié.

**Utilisation :**

`python3 anonloginftp.py`

Il va vous demander de rentrer l'IP de l'hôte auquel se connecter. Pour ce test, j'ai utilisé metasploitable.

## ftpbrute.py & passwordsftp.txt

Bruteforce la connexion en ftp à l'hôte spécifié grâce au fichier spécifié en entrée.

**Utilisation :**

`python3 ftpbrute.py`

Ensuite, il va vous demander l'hôte à cibler et le path vers le fichier de mots de passe (au format user:mdp). Pour ce test, j'ai utilisé metasploitable.