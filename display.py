# -*- coding: utf-8 -*-
import RPi_I2C_driver
import RPi.GPIO as GPIO
from time import *
import requests
import json
import pins
import threading
from unidecode import unidecode
import os
import sys

mylcd = RPi_I2C_driver.lcd()

#Affiche bonjour et Demarrage en cours
mylcd.lcd_display_string("Bonjour!", 1)
mylcd.lcd_display_string("Demarrage en cours", 2)

sleep(2) # 2 sec delay
mylcd.lcd_clear()
# Loop pour compte à rebours.
x = 9

#L'utilité de cette boucle est de permettre au raspberry pi de se connecter au réseau WiFi.

while x != 0:
    mylcd.lcd_display_string("Demarrage dans:", 2)
    mylcd.lcd_display_string("%s secondes " % (x),3)
    x = x-1
    sleep(1)
    
mylcd.lcd_clear()
sleep(2)
#lier les numéros au def du fichier pins.py
digit = {0 : pins.zero,1 : pins.one,2 : pins.two,3 : pins.three,4 : pins.four,5 : pins.five,6 : pins.six,7 : pins.seven,8 : pins.eight,9 : pins.nine}
digitD = {0 : pins.zeroD,1 : pins.oneD,2 : pins.twoD,3 : pins.threeD,4 : pins.fourD,5 : pins.fiveD,6 : pins.sixD,7 : pins.sevenD,8 : pins.eightD,9 : pins.nineD} 

#Icones personalisées
fontdata = [
    #snow flake
    [0x0a,0x04,0x15,0x0e,0x15,0x04,0x0a,0x00],
    #notication
    [0x1f,0x1b,0x1b,0x1b,0x1b,0x1f,0x1b,0x1f],
    #chaise roulante
    [0x1f,0x1d,0x1d,0x1d,0x11,0x15,0x15,0x1f],
]

#Charge les icones
mylcd.lcd_load_custom_chars(fontdata)


def numbers():
    # Crée un thread pour pouvoir faire d'autres opérations au même temps
    threading.Timer(10.0, numbers).start()
    #Récupère les données pour l'api TL pour la ligne 9
    url9 = "http://syn.t-l.ch/apps/LineStopDeparturesList?roid=3377704015495689&lineid=11821953316814886"
    response9 = requests.request("GET", url9)
    j9 = json.loads(response9.text)
    # Sélectionne l'élément nécessaire
    nextBus9 = j9["journeys"]['journey'][0]["waiting_time"]
    nextNextBus9 = j9["journeys"]['journey'][1]["waiting_time"]
    nextBus9AC = j9["journeys"]['journey'][0]["handicapped_access"]
    nextNextBus9AC = j9["journeys"]['journey'][1]["handicapped_access"]
    
    #Récupère les données pour l'api TL pour la ligne 8
    url8 = "http://syn.t-l.ch/apps/LineStopDeparturesList?roid=3377704015496073&lineid=11821953316814885"
    response8 = requests.request("GET", url8)
    j8 = json.loads(response8.text)
    # Sélectionne l'élément nécessaire
    nextBus8 = j8["journeys"]['journey'][0]["waiting_time"]
    nextNextBus8 = j8["journeys"]['journey'][1]["waiting_time"]
    nextBus8AC = j8["journeys"]['journey'][0]["handicapped_access"]
    nextNextBus8AC = j8["journeys"]['journey'][1]["handicapped_access"]
    
    # Maintenant que nous avons bien les données nous pouvons étaindre toutes les LED pour éviter des bugs d'affichage
    pins.reset()
    #Pratique pour débuger on imprime dans le terminal le prochain bus
    print nextBus9
    print nextBus9AC
    # Ici on cherche a ce que le troisime chiffre de XX:XX:XX soit = 0 celà veut dire que le bus est dans moins de 10 min
    if(int(nextBus9[3:4]) == 0):
        # Si c'est le cas ajouter le point et afficher le 4ème chiffre (en partant de 1) et le 5ème chiffre
        pins.dot()
        digitD[int(nextBus9[4:5])]()
        digit[int(nextBus9[6:7])]()
    else:
        #Afficher le temps en minutes.
        digitD[int(nextBus9[3:4])]()
        digit[int(nextBus9[4:5])]()
    #LED climatisation
    pins.ACoff()
    if nextBus9AC == "1":
        pins.AC()
    
    mylcd.lcd_clear()
    mylcd.lcd_display_string_pos("Ligne 9:",1,0)
    mylcd.lcd_display_string_pos("%s min." % (str(nextNextBus9[3:5])),1,11)
    
    if nextNextBus9AC == "1":
         mylcd.lcd_display_string_pos(chr(0),1,19)
   
    mylcd.lcd_display_string_pos("Ligne 8:",3,0)
    mylcd.lcd_display_string_pos("%s min." % (str(nextBus8[3:5])),4,0)
    mylcd.lcd_display_string_pos("%s min." % (str(nextNextBus8[3:5])),4,11)
    
    if nextBus8AC == "1":
         mylcd.lcd_display_string_pos(chr(0),4,8)
            
    if nextNextBus8AC == "1":
         mylcd.lcd_display_string_pos(chr(0),4,19)
    

        
def prob():
    # Crée un thread pour pouvoir faire d'autres opérations au même temps
    threading.Timer(20.0, prob).start()
    #Récupère les données pour l'api TL
    url = "http://syn.t-l.ch/apps/Messages?r=11821953316814886"
    responseM = requests.request("GET", url)
    m = json.loads(responseM.text)
    # Sélectionne l'élément nécessaire
    mes = m["messages"]
    #Vérifie si il y a une notification a afficher. 
    if mes == "{}":
        pins.red() #Allume la led rouge
    else:
        pins.redoff()


numbers()
prob()
