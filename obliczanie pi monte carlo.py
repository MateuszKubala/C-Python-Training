import random
import math

wkole=0
pozakolem=0
r=int(input("podaj promień: "))
print("promień = ",r)

bok=r*2
kwadrat=bok*bok
print("pole = ", kwadrat)

i=int(input("podaj liczbę punktów: "))


for wiersze in range (1,bok+1):
    for kolumny in range(1,bok+1):
        wynik=wiersze*kolumny
        #print(wynik,"\t",end="") "wyświetlanie pola kwadratu"
    print()
pi=math.pi
print("pi= ", pi)
powyzej=int(pi*(r*r))
ponizej=int(kwadrat-powyzej)
print("zakres: ", powyzej, " do ", ponizej)

for w in range(0,i):
    a=random.randint(0,kwadrat)
    #print("losowe liczby z zakresu: ",a,"\t", end="") "wyświetlanie liczb losowych"
    print() 
    if a in range(ponizej, powyzej):
        d=1
        wkole=wkole+d
    else:
        b=1
        pozakolem=pozakolem+b
        
print("w kole = ", wkole, "poza kołem = ", pozakolem)
promien=(pozakolem/wkole)*4
print("promien = ", promien)
        
    
