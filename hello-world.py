print ("Hallo, ich bin ein Computer")

name = input("Wie ist dein Name?")
print("Schoen dich zu treffen " ,name, ". Dein Name ist " ,len(name), " Zeichen lang.")

alter = input("Wie alt bist du?")
alter = int(alter)
if (alter > 100):
    print("Das ist wohl ein Scherz oder?")
else:
    print("Du wirst in einem Jahr ",int(alter)+1, " Jahre alt sein." )

print("Tschüss....")