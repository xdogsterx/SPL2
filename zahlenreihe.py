# Zahlenreihe.py
n = input("Bitte n eingeben: ")
n = int(n)
for i in range(1,n+1):
    if(i < n):
        print(i, end=" < ")
    else:
        print(i)