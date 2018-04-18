regen = True
regenschirm = True
eingabe2 =""
while (regen):
    eingabe = input("Regnet es?(ja/nein)")
    if (eingabe == "nein"):
        regen = False
        print("Geh nach draußen.")
    elif (eingabe == "ja"):
        if(eingabe2 == ""):
            eingabe2 = input("Hast du einen Regenschirm?(ja/nein)")
            if (eingabe2 == "ja"):
                print("Geh nach draußen.")
                regen = False
            else:
                regenschirm = False
                print("Warte ein bisschen.")
    else:
        print("bitte nur ja und nein eingeben")



        

       
