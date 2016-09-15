#! /usr/bin/python
# coding= utf-8

from scapy.all import *

def recuperer_infos_paquets(fichier_pcap):
	if fichier_pcap == "":
		fichier_pcap = "ailes_cassees.pcap"

	liste_paquets=rdpcap(fichier_pcap)
	i = 0
	for p in liste_paquets:
		print "Paquet", i
		if p.haslayer(Raw):
			print p.getlayer(Raw).load.encode('hex')
		else:
			print "Pas de Raw"
		i = i+1

	return liste_paquets