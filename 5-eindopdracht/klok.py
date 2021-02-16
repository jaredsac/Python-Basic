from turtle import *
import time


seconde = 58
minuten = 59
uren = 23


setup()
tl = Turtle()

while True:
    tl.clear()
    # met deze functie gebruik ik om het getalen niet over elkaar te schrijven.

    tl.write(str(uren).zfill(2) + ":" + str(minuten).zfill(2) + ":" + str(seconde).zfill(2),
             font=("times new roman", 25, "normal"))
    # hier dwing ik python om twee getalen te gebruiken en de font gebruik ik om het mooier te maken.

    seconde = seconde + 1
    time.sleep(1)
    # hier gaat de seconde met 1 optellen.

    if seconde == 60:
        seconde = 0
        minuten = minuten + 1
    # hier laat ik zien dat als seconde op 60 spring dan komt er een minuut bij.
    
    if minuten == 60:
        minuten = 0
        uren = uren + 1
    # nu doet de functie als het 60 minuten bereikt dan komt er 1 bij de de uren.
    
    if uren == 24:
        uren = 0
    # hier doe ik dus als de uren op 24 springt dat show het 00 in plaats van 24.
