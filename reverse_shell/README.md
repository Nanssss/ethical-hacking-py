# Reverse Shell

Ce projet est un cheval de troie constitué de 2 programmes :

## server.py

C'est le programme à exécuter par l'attaquant. C'est un serveur qui attend un connexion par une machine victime.
Une fois la connexion établie, il peut exécuter tout un tas de commandes, qu'on peut lister en utilisant la commande "help".
            download <path> --> Download a file from target PC
            upload <path>   --> Upload a file to target PC
            get <url>       --> Download a file to target PC from a url
            start path      --> Start a program on target pc
            screenshot      --> Take a screenshot of target monitor
            check           --> Check for the admin privileges
            keylog_start    --> Start the keylogger on target PC
            keylog_dump     --> Dump the keylogger collected data
            q               --> exit the reverse shell '''

## target.py

Programme à lancer sur la machine victime. Il va établir un connexion avec l'attaquant, qui aura accès aux commandes précedemment citées.

