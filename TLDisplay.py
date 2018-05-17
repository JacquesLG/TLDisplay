# -*- coding: utf-8 -*-
import RPi_I2C_driver
import RPi.GPIO as GPIO
from time import *
import requests
import json
import pins
import threading
import unidecode

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
    
#lier les numéros au def du fichier pins.py
digit = {0 : pins.zero,1 : pins.one,2 : pins.two,3 : pins.three,4 : pins.four,5 : pins.five,6 : pins.six,7 : pins.seven,8 : pins.eight,9 : pins.nine}
digitD = {0 : pins.zeroD,1 : pins.oneD,2 : pins.twoD,3 : pins.threeD,4 : pins.fourD,5 : pins.fiveD,6 : pins.sixD,7 : pins.sevenD,8 : pins.eightD,9 : pins.nineD} 

def numbers():
    # Crée un thread pour pouvoir faire d'autres opérations au même temps
    threading.Timer(10.0, numbers).start()
    #Récupère les données pour l'api TL
    url = "http://syn.t-l.ch/apps/LineStopDeparturesList?roid=3377704015495689&lineid=11821953316814886"
    response = requests.request("GET", url)
    j = json.loads(response.text)
    # Sélectionne l'élément nécessaire
    nextBus = j["journeys"]['journey'][0]["waiting_time"]
    # Maintenant que nous avons bien les données nous pouvons étaindre toutes les LED pour éviter des bugs d'affichage
    pins.reset()
    pins.red()
    #Pratique pour débuger on imprime dans le terminal le prochain bus
    print nextBus
    # Ici on cherche a ce que le troisime chiffre de XX:XX:XX soit = 0 celà veut dire que le bus est dans moins de 10 min
    if(int(nextBus[3:4]) == 0):
        # Si c'est le cas ajouter le point et afficher le 4ème chiffre (en partant de 1) et le 5ème chiffre
        pins.dot()
        digitD[int(nextBus[4:5])]()
        digit[int(nextBus[6:7])]()
    else:
        #Afficher le temps en minutes.
        digitD[int(nextBus[3:4])]()
        digit[int(nextBus[4:5])]()
        
def screen():
    # Crée un thread pour pouvoir faire d'autres opérations au même temps
    threading.Timer(300.0, numbers).start()
    #Récupère les données pour l'api TL
    url = "http://syn.t-l.ch/apps/Messages?r=11821953316814886"
    responseM = requests.request("GET", url)
    m = json.loads(responseM.text)
    # Sélectionne l'élément nécessaire
    mes = m["messages"]
    #Vérifie si il y a une notification a afficher. 
    if mes:
        pins.red() #Allume la led rouge
        mylcd.lcd_display_string("%d", % (unicode.unidecode(m["messages"]["message"][0]["content"]))
        
    else:
        pins.redoff() 
    


numbers()
screen

