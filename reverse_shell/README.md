# Reverse Shell

Ce projet est un cheval de Troie (Trojan) constitué de 3 programmes : server.py, target.py et keylogger.py.

Le Trojan est un type de logiciel malveillant particulièrement dangereux. Il consiste à installer un "parasite" sur la machine de la victime, en prenant l'apparence d'un programme sain et légitime. Ce parasite permettra d'exécuter toutes sortes d'actions malveillantes à l'insu de l'utilisateur. Dans ce cheval de Troie, je peux entre autres récupérer les touches de clavier pressées, prendre des screenshots, télécharger et uploader des fichiers sur la machine cible, et même avoir accès à l'invite de commande (avec lequel on peut pratiquement tout faire).


## server.py

C'est le programme à exécuter par l'attaquant. C'est un serveur qui attend un connexion par une machine victime.
Une fois la connexion établie, il peut exécuter tout un tas de commandes, qu'on peut lister en utilisant la commande "help" :

            `download <path> --> Download a file from target PC
            upload <path>   --> Upload a file to target PC
            get <url>       --> Download a file to target PC from a url
            start path      --> Start a program on target pc
            screenshot      --> Take a screenshot of target monitor
            check           --> Check for the admin privileges
            keylog_start    --> Start the keylogger on target PC
            keylog_dump     --> Dump the keylogger collected data
            q               --> exit the reverse shell '''`

**Utilisation :**

Avant de lancer le programme, l'ouvrir et remplacer (tout en haut) localIP par l'IP de l'attaquant (donc de votre machine), pour le port vous pouvez choisir ce que vous voulez. Ensuite, exécuter le programme :

`sudo python3 server.py`

Le serveur est donc lancé et attend la connexion d'une victime.

## target.py

Programme à lancer sur la machine victime. Il va établir un connexion avec l'attaquant, qui aura accès aux commandes précedemment citées.

Ce programme n'est en soit que le parasite expliqué plus haut, il ne prend pas l'apparrence d'un autre logiciel sain. Cependant, j'ai pu faire des tests, et j'ai remarqué que je pouvais injecter ce code dans n'importe quel exécutable. Toute machine exécutant celui-ci se retrouvant alors infectée.

**Utilisation :**

Avant de lancer le programme, l'ouvrir et remplacer (tout en haut) localIP par l'IP de l'attaquant, pour le port vous pouvez choisir ce que vous voulez. Ensuite, exécuter le programme (vous pouvez exécuter les 2 programmes sur la même machine) :

`sudo python3 target.py`

La victime va se connecter à l'attaquant. Une fois la connexion effectuée, celui-ci pourra effectuer de nombreuses commandes. Tapez "help" pour avoir la liste des commandes.

## keylogger.py

Un keylogger, ce programme est utilisé par le cheval de Troie.