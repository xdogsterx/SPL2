#zahlenraten.py

import random
zufallszahl = random.randint(1,100)
# Benutzer soll die Zahl vom Computer erraten
while (True):
    versuch = input("Geben Sie ihre schätzung ein: ")
    if(versuch == zufallszahl):
        print("Gratulation")
        break
    else:
        print("Versuchen Sie es erneut")
    
# Ausgabe: wie viele Versuche waren nötig?