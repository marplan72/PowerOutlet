#!/usr/bin/env python                                                                                                                                                             
# -*- coding: utf-8 -*-
#
# PROGRAMME.......: poweroutlet8chl.py
# VERSION.........: 1.0.0
# DATE DE CREATION: 2015-02-07
# DATE DE CREATION: 2015-02-07
# UTILISATION.....: Gestion des prises electrique avec un relay 8 channel
#
 
# Historique des versions
#
# 2015-02-07 - Creation

import RPi.GPIO as GPIO
import time
import random
import sys
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinList = [17, 18, 27, 22, 23, 24, 25, 4]
# Ordre :   0,  1,  2,  3,  4,  5,  6, 7
sListe = ["Socket s1", 
          "Socket s2",
          "Socket s3",
          "Socket s4",
          "Socket s5",
          "Socket s6",
          "Socket s7",
          "Socket s8"]
SleepTimeL = 0.2
sCfgFil = "/var/www/gpio8/poweroutlet.cfg"


###############################################################################
#
# FONCTION: wlog
# MODULE APPELLANT: Multiple
# OBJECTIF: Afficher date et heure suivi d'un commentaire
#
###############################################################################
def wlog(ligne):
   print (time.strftime("%Y-%m-%d %H:%M:%S - ") + ligne)

###############################################################################
#
# FONCTION: fexiste
# OBJECTIF: Retourne vrai si le fichier recu existe.
# ENTREE..: Nom de fichier
# SORTIE..: Boolean
# MODULE APPELLANT: Multiple
#
###############################################################################
def fexiste(sFic):
    # On met la valeur a faux
    bFicVal = False
    try:
        # On tente d'ourir le fichier. Si succes, on met la valeur a vrai.
        with open(sFic, 'r') as f:
            read_data = f.read()
            bFicVal = True
        f.closed
		
    finally:
        # On retourne la valeur.
	return bFicVal
   
###############################################################################
#
# FONCTION: gauche0
# MODULE APPELLANT: Main
# OBJECTIF: Active un socket un a la fois vers la gauche.
#
###############################################################################
def gauche0():
	wlog("Appuyez sur CTRL + C pour terminer")
	for i in pinList: 
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.LOW)		
	try:
		while True:
			for i in pinList:
				GPIO.output(i, GPIO.HIGH)
				time.sleep(SleepTimeL);
				GPIO.output(i, GPIO.LOW)

	except KeyboardInterrupt:
		print '\n'
		GPIO.cleanup()

###############################################################################
#
# FONCTION: gauche1
# MODULE APPELLANT: Main
# OBJECTIF: Active les sockets vers la gauche et les desactivent a la fin.
#
###############################################################################
def gauche1():
	wlog("Appuyez sur CTRL + C pour terminer")
	for i in pinList: 
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.LOW)		
	try:
		while True:
			for i in pinList:
				GPIO.output(i, GPIO.HIGH)
				time.sleep(SleepTimeL);
				
			for i in pinList:
				GPIO.output(i, GPIO.LOW)
			time.sleep(SleepTimeL);

	except KeyboardInterrupt:
		print '\n'
		GPIO.cleanup()
		
###############################################################################
#
# FONCTION: droite0
# MODULE APPELLANT: Main
# OBJECTIF: Active un socket a la fois vers la droite.
#
###############################################################################
def droite0():
	wlog("Appuyez sur CTRL + C pour terminer")
	for i in pinList: 
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.LOW)		
	pinList.reverse()
	
	try:
		while True:
			for i in pinList:
				GPIO.output(i, GPIO.HIGH)
				time.sleep(SleepTimeL);
				GPIO.output(i, GPIO.LOW)

	except KeyboardInterrupt:
		print '\n'
		GPIO.cleanup()

###############################################################################
#
# FONCTION: droite1
# MODULE APPELLANT: Main
# OBJECTIF: Active les socket vers la droite et les desactivent a la fin.
#
###############################################################################
def droite1():
	wlog("Appuyez sur CTRL + C pour terminer")
	for i in pinList: 
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.LOW)		
	pinList.reverse()
	
	try:
		while True:
			for i in pinList:
				GPIO.output(i, GPIO.HIGH)
				time.sleep(SleepTimeL);
			
			for i in pinList:
				GPIO.output(i, GPIO.LOW)
			time.sleep(SleepTimeL);

	except KeyboardInterrupt:
		print '\n'
		GPIO.cleanup()

###############################################################################
#
# FONCTION: aleatoire
# MODULE APPELLANT: Main
# OBJECTIF: Active et desactive un socket de facon aleatoire sans repeter le
# dernier socket.
#
###############################################################################
def aleatoire():	
	wlog("Appuyez sur CTRL + C pour terminer")
	
	for i in pinList: 
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.LOW)

	iOldPin = 0
	iPin = 0
		
	try:
		while True:
			while iPin == iOldPin:
				iPin = random.choice(pinList)				
			GPIO.output(iPin, GPIO.HIGH)
			time.sleep(SleepTimeL);
			GPIO.output(iPin, GPIO.LOW)
			iOldPin = iPin
	  
	except KeyboardInterrupt:
		print '\n'
		GPIO.cleanup()

###############################################################################
#
# FONCTION: etat
# MODULE APPELLANT: Main
# OBJECTIF: Affiche l'etat de chaque gpio
#
###############################################################################
def etat():
	# Initialisation de chaque gpio
	for i in pinList: 
		GPIO.setup(i, GPIO.OUT)

	wlog("Etat acutel des sockets:")
	
	if GPIO.input(17) != GPIO.HIGH:
		wlog(sListe[0] + " est OFF.")
	else:
	    wlog(sListe[0] + " est ON.")
	    	
	if GPIO.input(18) != GPIO.HIGH:
		wlog(sListe[1] + " est OFF.")
	else:
	    wlog(sListe[1] + " est ON.")
	    
	if GPIO.input(27) != GPIO.HIGH:
		wlog(sListe[2] + " est OFF.")
	else:
	    wlog(sListe[2] + " est ON.")
	    
	if GPIO.input(22) != GPIO.HIGH:
		wlog(sListe[3] + " est OFF.")
	else:
	    wlog(sListe[3] + " est ON.")
	    
	if GPIO.input(23) != GPIO.HIGH:
		wlog(sListe[4] + " est OFF.")
	else:
	    wlog(sListe[4] + " est ON.")
	    
	if GPIO.input(24) != GPIO.HIGH:
		wlog(sListe[5] + " est OFF.")
	else:
	    wlog(sListe[5] + " est ON.")
	    
	if GPIO.input(25) != GPIO.HIGH:
		wlog(sListe[6] + " est OFF.")
	else:
	    wlog(sListe[6] + " est ON.")
	    
	if GPIO.input(4) != GPIO.HIGH:
		wlog(sListe[7] + " est OFF.")
	else:
	    wlog(sListe[7] + " est ON.")

###############################################################################
#
# FONCTION: Reset
# MODULE APPELLANT: Main
# OBJECTIF: Fait un reset des relais de la carte
#
###############################################################################
def Reset():

	for i in pinList: 
		GPIO.setup(i, GPIO.OUT) 
		GPIO.output(i, GPIO.LOW)
	GPIO.cleanup()
	wlog("Reset des sockets.")

###############################################################################
#
# FONCTION: ForAll
# MODULE APPELLANT: Main
# OBJECTIF: Applique l'action recu sur tous les sockets.
#
###############################################################################
def ForAll(Action):
	for i in pinList:
		GPIO.setup(i, GPIO.OUT)
		
	if sys.argv[2] == 'on':
		for i in pinList:			
			GPIO.output(i, GPIO.HIGH)
                wlog("Tous les sockets sont a ON.")
	else:
		for i in pinList:
			GPIO.output(i, GPIO.LOW)
                wlog("Tous les sockets sont a OFF.")

###############################################################################
#
# FONCTION: OnOff
# MODULE APPELLANT: Main
# OBJECTIF: Met le GPIO recu On ou Off selon le parametre passe au pgm.
#
###############################################################################
def OnOff(iGpio, sSocket):
    GPIO.setup(iGpio, GPIO.OUT)

    # On verifie l'etat du socket.
    if GPIO.input(iGpio) == 0:
            State = "OFF"
    else:
            State = "ON"

    # On met l'etat le GPIO recu a l'etat voulu en argv[2].
    if sys.argv[2].lower() == 'on':
          GPIO.output(iGpio, GPIO.HIGH)
          wlog(sSocket + " " + sys.argv[1] + " passe de " + State + " a ON.")
    else:
          GPIO.output(iGpio, GPIO.LOW)
          wlog(sSocket + " " + sys.argv[1] + " passe de " + State + " a OFF.")

###############################################################################
#
# FONCTION: LireFichier
# MODULE APPELLANT: Etat
# OBJECTIF: Lire le fichier de configuration
#
###############################################################################
def LireFichier ():
    # Si le fichier de config existe, on va le lire.
    # Le cas echeant, on utilise les valeurs buit-in
    if fexiste(sCfgFil):
        i = 0         
        fic = open(sCfgFil, "r")
        for line in fic:
            sListe[i] = line.strip()
            i += 1

###############################################################################
#
# FONCTION: clignote
# MODULE APPELLANT: Main
# OBJECTIF: Fait clignoter le gpio recu en parametre.
#
###############################################################################
def clignote(iGpio, sNomSocket):
    wlog("Clignotement de " + sNomSocket + ". Appuyez sur CTRL + C pour terminer")
    GPIO.setup(iGpio, GPIO.OUT)
    GPIO.output(iGpio, GPIO.LOW)
          
    try:
          while True:
                 GPIO.output(iGpio, GPIO.HIGH)
                 time.sleep(SleepTimeL);
                 GPIO.output(iGpio, GPIO.LOW)
                 time.sleep(SleepTimeL);
          
    except KeyboardInterrupt:
                 print '\n'
                 GPIO.output(iGpio, GPIO.LOW)

###############################################################################
#
# FONCTION: 
# MODULE APPELLANT: 
# OBJECTIF: 
#
###############################################################################
#def MaFctn ():


###############################################################################
#
#       +---+---+---+---+---+---+---+---+---+---+---+
#       | M | A | I | N |   | M | O | D | U | L | E |
#       +---+---+---+---+---+---+---+---+---+---+---+
#
###############################################################################

# Lecture du fichier de config.
LireFichier()

# Si aucun parametre recu, on affiche l'etat.
if len(sys.argv) == 1:
        etat()	    

# Permet de refaire un reset des relais.
elif sys.argv[1] == '-reset':
        Reset()
	
# Action a faire sur le socket recu.
elif sys.argv[1] == 's1':
        OnOff(17, sListe[0])
		
elif sys.argv[1] == 's2':
        OnOff(18, sListe[1])
		
elif sys.argv[1] == 's3':
        OnOff(27, sListe[2])

elif sys.argv[1] == 's4':
        OnOff(22, sListe[3])
		
elif sys.argv[1] == 's5':
        OnOff(23, sListe[4])
		
elif sys.argv[1] == 's6':
        OnOff(24, sListe[5])
		
elif sys.argv[1] == 's7':
        OnOff(25, sListe[6])
		
elif sys.argv[1] == 's8':
        OnOff(4, sListe[7])

# Faire une action pour tous les sockets.
elif sys.argv[1] == 'all':
        ForAll(sys.argv[2])

# Fantasie.
elif sys.argv[1] == '-g0':
	gauche0()

elif sys.argv[1] == '-g1':
	gauche1()
			
elif sys.argv[1] == '-d0':
	droite0()

elif sys.argv[1] == '-d1':
	droite1()

elif sys.argv[1] == '-r': 
        aleatoire() 

elif sys.argv[1] == '-c':
        if sys.argv[2] == 's1':
           clignote(17, sListe[0])
        elif sys.argv[2] == 's2':
           clignote(18, sListe[1])
        elif sys.argv[2] == 's3':
           clignote(27, sListe[2])
        elif sys.argv[2] == 's4':
           clignote(22, sListe[3])
        elif sys.argv[2] == 's5':
           clignote(23, sListe[4])
        elif sys.argv[2] == 's6':
           clignote(24, sListe[5])
        elif sys.argv[2] == 's7':
           clignote(25, sListe[6])
        elif sys.argv[2] == 's8':
           clignote(4, sListe[7])
        else:
           wlog("Socket invalide.")

# Si les parametres ne sont pas connus...
else:
    wlog("Le(s) parametre(s) recu(s) est(sont) invalide(s).")
    wlog("Parametres attendus: sX ou X est le # de socket entre 1 et 8, [on/off]")
    wlog("-g0/-g1: Active les prises vers la gauche;")
    wlog("-d0/-d1: Active les prises vers la droite;")
    wlog("-r.....: Active une prise de facon aleatoire;")
    wlog("-reset.: Fait un reset pour desactiver les prises.")
exit (0)
