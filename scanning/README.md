# Scanning

Divers outils pour scanner les ports. 

En informatique, un port logiciel (à ne pas confondre avec les ports matériels, ex USB), sont des sortes de "portes d'entrées". En effet, lors de communications en réseau, différents ordinateurs s'échangent des données par la même IP, qui sont destinées à des applications distinctes. Pour pouvoir savoir à quelle application telle donnée est destinée, on utilise la notion de port.

Ils sont codés sur 16 bits, il y a donc 65536 ports. Les ports de 0 à 1023 sont réservés aux services les plus courants, ceux de 1024 à 49151 correspondent aux ports enregistrés (mais sont tout de même modifiables), et les ports de 49152 à 65536 correspondent aux ports dynamiques.

Les scanners de ports, comme leur nom l'indique, scannent tous les ports d'une machine afin de savoir lesquels sont ouverts ou fermés. Pour chaque port ouvert, ils peuvent analyser les réponses obtenues afin d'obtenir des informations sur les applications communiquant par ces ports, qui comportent d'éventuelles failles de sécurité.

Il est donc possible avec cet outil de cartographier un réseau et d'y trouver des vulnérabilités.

## portscan1.py

Essaye tout simplement de se connecter à un port (spécifié en dur dans le code) de l'IP spécifié.
Affiche en sortie si le port est ouvert ou fermé.

## portscan2.py

Idem sauf que le programme prend en paramètre l'IP de la machine cible et le port à portscanner

## portscan3.py

Idem mais scanne tous les ports de 1 à 1000

## advancescanner.py

Juste un test pour optparse

## advancescanner2.py

Utilise optparse pour prendre des arguments en entrée, -H <hostname> et -p <port1,port2...>
Scanne les ports de l'IP/Host spécifié

## retbanner.py

Scanne les ports 1 à 100 d'une IP spécifiée. En plus de la connection au port, on regarde le retour du port, qu'on affiche s'il est ouvert.

## vulnscan.py & vulnbanner.txt

Le fichier prend en entrée un fichier .txt contenant une liste de vulnérabilités connues.
Il scanne ensuite une série d'ips et de ports comme dans retbanner.py, puis si une banner est retournée, il cherche si celle si existe dans le fichier de vulnérabilités connues.
On aura alors trouvé une vulnérabilité.
