#! /usr/bin/python
# coding= utf-8

from scapy.all import *

def recuperer_infos_paquets(fichier_pcap):
	if fichier_pcap == "":
		fichier_pcap = "ailes_cassees.pcap"

	liste_paquets=rdpcap(fichier_pcap)
	i = 0
	id_objet = ""
	prix_objet = []
	#les paquets commencent a 0
	for p in liste_paquets:
		data = ""

		#print "Paquet", i

		#si le paquet contient un data
		if p.haslayer(Raw):
			data = p.getlayer(Raw).load.encode('hex')
			#print data

			#paquet contenant l'ID du l'objet (paquet no 2)
			if "5abd02" in data:
				id_objet = data[6:]
				print "ID objet :", id_objet

			#paquet contenant les prix de l'objet (paquet no 3)
			if "636904a" in data and len(data)>50:
				prix_objet.append(str(int(data[38:46], 16)) + 'k')
				prix_objet.append(str(int(data[46:54], 16)) + 'k')
				prix_objet.append(str(int(data[54:62], 16)) + 'k')
				print "Prix :", prix_objet

		i = i+1

	return (id_objet, prix_objet)