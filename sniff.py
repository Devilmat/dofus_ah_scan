from scapy.all import *

adresse_serveur = '213.248.126.78'
f = open('prix.txt', 'w')
def packet_callback(p):
	if p.haslayer(Raw):
		prix_objet = []
		data = p.getlayer(Raw).load.encode('hex')
		#paquet contenant l'ID de l'objet
		if "5abd02" in data:
			id_objet = data[6:]
			print id_objet
			f.write(id_objet+'\n')

		#paquet contenant les prix de l'objet (paquet no 3)
		if "6369" in data:
			if data[38:46] != '':
				prix_objet.append(str(int(data[38:46], 16)))
			if data[46:64] != '':
				prix_objet.append(str(int(data[46:54], 16)))
			if data[54:62] != '':
				prix_objet.append(str(int(data[54:62], 16)))
			if len(prix_objet) != 0:
				print prix_objet[0]+' '+prix_objet[1]+' '+prix_objet[2]
				f.write(prix_objet[0]+' '+prix_objet[1]+' '+prix_objet[2]+'\n')
				

sniff(filter='host %s'%adresse_serveur, prn=packet_callback)
