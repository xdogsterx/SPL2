#zahlenraten.py

import random
zufallszahl = random.randint(1,10)
versuch = False
# Benutzer soll die Zahl vom Computer erraten
while (versuch == False):
    versuch = input("Geben Sie ihre schätzung ein: ")
    if(int(versuch) == zufallszahl):
        print("Gratulation")
        
    else:
        print("Versuchen Sie es erneut")
    
# Ausgabe: wie viele Versuche waren nötig?