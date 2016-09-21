#!/usr/bin/python
# -*- coding: utf-8 -*-
from scapy.all import *

from recuperer_infos_paquets import recuperer_infos_paquets

(id_objet, prix_objet) = recuperer_infos_paquets("ailes_moskito.pcap")


