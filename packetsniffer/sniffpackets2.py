#!usr/bin/python3

import socket
import os,sys
import struct
import binascii
from termcolor import colored


sock_created = False
sniffer_socket = 0



def analyze_udp_header(data_recv):

	udp_hdr = struct.unpack('!4H',data_recv[:8])
	src_port = udp_hdr[0]
	dst_port = udp_hdr[1]
	length = udp_hdr[2]
	checksum = udp_hdr[3]
	data = data_recv[8:]

	print(colored("_______________________UDP HEADER_______________________",'magenta','on_yellow'))
	print("Source: %hu " % src_port)
	print("Destination: %hu " % dst_port)
	print("Length: %hu " % length)
	print("Checksum : %hu " % checksum)

	return data


def analyze_tcp_header(data_recv):

	tcp_hdr = struct.unpack('!2H2I4H', data_recv[:20])
	src_port = tcp_hdr[0]
	dst_port = tcp_hdr[1]
	seq_num = tcp_hdr[2]
	ack_num = tcp_hdr[3]
	data_offset = tcp_hdr[4] >> 12
	reserved = (tcp_hdr[4] >> 6) & 0x03ff
	flags = tcp_hdr[4] & 0x003f
	window = tcp_hdr[5]
	checksum = tcp_hdr[6]
	urg_ptr = tcp_hdr[7]
	data = data_recv[20:]

	urg = bool(flags & 0x0020)
	ack = bool(flags & 0x0010)
	psh = bool(flags & 0x0008)
	rst = bool(flags & 0x0004)
	syn = bool(flags & 0x0002)
	fin = bool(flags & 0x0001)

	print(colored("___________________TCP HEADER_________________",'magenta','on_yellow'))
	print("Source: %hu " % src_port)
	print("Destination: %hu " % dst_port)
	print("Seq: %u " % seq_num)
	print("Ack: %u " % ack_num)
	print("Flags: ")
	print("URG: %d " % urg)
	print("ACK: %d " % ack)
	print("PSH: %d " % psh)
	print("RST: %d " % rst)
	print("SYN: %d " % syn)
	print("FIN: %d " % fin)
	print("Windsize: %hu " % window)
	print("Checksum: %hu " % checksum)

	return data



def analyze_IP_header(data_recv):

	ip_hdr = struct.unpack('!6H4s4s',data_recv[:20])
	ver = ip_hdr[0] >> 12 #12 bits
	ihl = (ip_hdr[0] >> 8) & 0x0f #garde pas ce qui a avant ni apres
	tos = ip_hdr[0] & 0x00ff
	tot_len = ip_hdr[1]
	ip_id = ip_hdr[2]
	flags = ip_hdr[3] >> 13
	frag_offset = ip_hdr[3] & 0x1fff
	ip_ttl = ip_hdr[4] >> 8
	ip_proto = ip_hdr[4] & 0x00ff
	checksum = ip_hdr[5]
	src_address = socket.inet_ntoa(ip_hdr[6]) #transforme l'adresse en string
	dst_address = socket.inet_ntoa(ip_hdr[7])
	data = data_recv[20:] #on garde que la data et on enleve le header ip

	print(colored("__________________IP HEADER_________________",'magenta','on_yellow'))
	print("Version: %hu " % ver)
	print("IHL: %hu " % ihl)
	print("TOS: %hu " % tos)
	print("Length: %hu" % tot_len)
	print("ID: %hu " % ip_id)
	print("Offset: %hu " % frag_offset)
	print("TTL: %hu " % ip_ttl)
	print("Proto : %hu " % ip_proto)
	print("Checksum : %hu " % checksum)
	print("Source IP : %s " % src_address)
	print("Destination IP: %s " % dst_address)

	if ip_proto == 6:
		tcp_udp = "TCP"
	elif ip_proto == 17:
		tcp_udp = "UDP"
	else:
		tcp_udp = "OTHER"

	return data, tcp_udp


def analyze_ether_header(data_recv):
	ip_bool = False #on le mettra a True si la fonction est un succes

	eth_hdr = struct.unpack('!6s6sH',data_recv[:14]) #voir table struct: 6s les adr mac source et cible, H le protocole ; 14 premiers = header ethernet
	dest_mac = binascii.hexlify(eth_hdr[0]) #transforme l'adresse mac en hexadecimal
	src_mac = binascii.hexlify(eth_hdr[1])
	proto = eth_hdr[2] >> 8 #il ne sait pas pk 8, 8 = ipv4
	data = data_recv[14:] #data = le reste

	print(colored("_____________________ETHERNET HEADER____________________",'magenta','on_yellow'))
	print("Destination MAC: %s:%s:%s:%s:%s:%s " % (dest_mac[0:2],dest_mac[2:4],dest_mac[4:6],dest_mac[6:8],dest_mac[8:10],dest_mac[10:12]))
	print("Source MAC: {}:{}:{}:{}:{}:{} ".format(src_mac[0:2],src_mac[2:4],src_mac[4:6],src_mac[6:8],src_mac[8:10],src_mac[10:12]))
	print("PROTOCOL: %hu" % proto)

	if proto == 0x08: #si c'est un protocole ipv4, donc ip header
		ip_bool = True

	return data, ip_bool



def main():

	global sock_created
	global sniffer_socket
	if sock_created == False:
		sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003)) #on prend le packet entier
		sock_created = True

	data_recv = sniffer_socket.recv(2048) #nbre de bits qu'on veut recevoir
	os.system('clear')

	data_recv, ip_bool = analyze_ether_header(data_recv) #on analyse l'header ethernet du packet recu
	if ip_bool: #si c'est vrai c'est qu'il y a un iP header et on va l'analyser
		data_recv, tcp_udp = analyze_IP_header(data_recv) #ici data recv est le data de analyze_ether_header, il contient la data restante , pas le header ether
	else:
		return

	if tcp_udp == "TCP":
		data_recv = analyze_tcp_header(data_recv)
	elif tcp_udp == "UDP":
		data_recv = analyze_udp_header(data_recv)
	else: # si le protocole est other
		return


while True:
	main()
