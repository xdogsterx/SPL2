# Zahlenreihe.py
n = input("Bitte n eingeben: ")
n = int(n)
for i in range(1,n+1):
    if(i < n):
        print(i, end=" < ")
    else:
        print(i)


for i in range(1,n+1):
    # alle ungeraden Zahlen von 1 bis n ausgeben
    if (i % 2):
        print (i, end=" ")

print("")

for i in range(1,n+1):
    # alle geraden Zahlen von 1 bis n ausgeben
    if (i % 2 == 0):
        print (i, end=" ")
    
print("")
# alle Zahlen von 1 bis n ausgeben, die durch 9 teilbar sind
for i in range(1,n+1):
    if(i%9 == 0):
        if(i+1 !=n):
            print(i, end=", ")
        else:
            print(i)
        
