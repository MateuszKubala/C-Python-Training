def main():

    
    liczba_prob = 5
    haslo = (input("podaj hasło: "))
    dlugosc_hasla = len(haslo)+1
    print("długość hasła: ", dlugosc_hasla-1)
    haslo_lista1 = []
    for litera in haslo:
        haslo_lista1.append(litera)
    
    haslo_lista=[]
    liczba=1
    while liczba < dlugosc_hasla:
        haslo_lista.append("_")
        liczba+=1

    print(haslo_lista)
    
    while liczba_prob != 0:
        litera = input("podaj literę: ")
        if litera in haslo_lista1:
            print ("trafiony")
            indeks=(haslo.index(litera))
            
            haslo_lista.remove("_")
            haslo_lista.insert(indeks, litera)
            
            print(haslo_lista)
            print("pozosało ci: ",liczba_prob, "prób")

            haslo_lista1.remove(litera)
           
            if haslo_lista1 == []:
                print("koniec, wygrałeś")

                break
         
        if litera not in haslo_lista1:
            print("błąd, straciłeś jedną próbę")
            liczba_prob-=1
            print("liczba prób: ", liczba_prob)

        if liczba_prob == 0:
            print("przegrałeś")
        


main()
