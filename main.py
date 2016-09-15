#!/usr/bin/python
# -*- coding: utf-8 -*-

from recuperer_infos_paquets import recuperer_infos_paquets

print "Premier pcap"
liste1 = recuperer_infos_paquets("ailes_cassees.pcap")
print "\n\nDeuxieme pcap"
liste2 = recuperer_infos_paquets("ailes_moskito.pcap")

for i in range(0, len(liste1)):
	print "Paquet",i
	if liste1[i].haslayer(Raw):
		print liste1[i].getlayer(Raw).load.encode('hex')
	else:
		print "Pas de Raw"
	if liste2[i].haslayer(Raw):
		print liste2[i].getlayer(Raw).load.encode('hex')
	else:
		print "Pas de Raw"