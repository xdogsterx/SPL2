# Zahlenreihe.py
n = input("Bitte n eingeben: ")
n = int(n)
for i in range(1,n+1):
    if(i < n):
        print(i, end=" < ")
    else:
        print(i)

n
for i in range(1,n+1):
    # alle ungeraden Zahlen von 1 bis n ausgeben
    if (i % 2):
        print (i, "ist ungerade")
    # alle geraden Zahlen von 1 bis n ausgebe
    
    
    
# alle Zahlen von 1 bis n ausgeben, die durch 9 teilbar sind