# Ethical Hacking Programs

⚠️ ***Ethical use only:** See `DISCLAIMER.md`. This code is for education and authorized testing only. The author is not responsible for misuse.

*Please keep in mind that I wrote this code back when I was still a student — it’s far from perfect!*

Also note that your antivirus may flag `target.py` as a Trojan, because it is indeed one! It is more precisely a reverse-shell your want to play with, so you're safe discarding your antivirus' warning.

----

**Attention, de nombreux programmes ne marchent que sous Linux.**

**Il y a aussi quelques dépendances à installer. Pour ce faire, il faut juste exécuter la commande `pip3 install -r requirements.txt`, j'espère ne pas en avoir oublié.**

**De plus, pour certains tests, j'utilisais une machine virtuelle faisant tourner metasploitable (une machine volontairement vulnérable), vous pouvez la trouver ici : https://sourceforge.net/projects/metasploitable/.**

Voici une description des programmes présents dans les sous-dossiers. A l'intérieur de chaque sous-dossier, vous avez un README expliquant le fonctionnement de chaque programme.

## scanning
Scanners de ports.

## sshftp
Programmes de login automatique en ftp et ssh, ainsi que des bruteforcers.

## passwordcracking
Programmes de cryptage et de bruteforce.

## bruteforce
Bruteforcers pour sites webs et gmail, ainsi que des programmes pour trouver les subdomains et directories d'un site web.

## localnetworkprograms
ARP Spoofer, sniffers HTTP, FTP, MAC, ainsi qu'un Synflooder.

## packetsniffer
Sniffer des paquets réseaux passant par la machine.

## dns
Sniffer DNS et un DNS Spoofer.

## wifi_passwds
Programme récupérant les mots de passe réseaux enregistrés sur la machine, et me les envoie par mail.

## reverse_shell
Trojan/Cheval de Troie.
