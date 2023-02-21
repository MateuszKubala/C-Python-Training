def main():
    file=open("todo.txt", "w")
    def wyswietlanie():
        print()
        nrzadania=0
        for zadanie in lista_zadan:
            print("indeks: ", nrzadania,"tresc:", zadanie)
            nrzadania+=1
        print()
            
    def nowe_zadanie():
        print()
        nowe=input("Podaj treść: ")
        print()
        lista_zadan.append(nowe)
        print("zaktualizowana lista zadań: ", lista_zadan)
        print()
        print("Zadanie :", nowe, "zostało dodane")
        print()
    
    def usun_zadanie():
        print()
        print("podaj numer od 0 do ",(len(lista_zadan)-1))
    
        wyswietlanie()
        usun=int(input("Podaj indeks: "))
        if usun in range(0,len(lista_zadan)):
            print()
            lista_zadan.pop(usun)
            print(lista_zadan)
        else:
            print()
            print("nie znaleziono tego numeru","\n")
    
    def zapisz_do_pliku():
        file = open("todo.txt", "w")
        for task in lista_zadan:
            file.write(task)
        file.close()
        print()
        print("zapisano")
        print()

    lista_zadan=[]

    def wczytywanie():
        file=open("todo.txt")
        for task in file.readlines():
            lista_zadan.append(task)
        file.close()
        print()
        print("pomyślnie zaktualizowano listę")
        print()
    wczytywanie()
    a=()
    while a!=5:
 
        if a== 1:
            wyswietlanie()
        
        if a == 2:
            nowe_zadanie()
        if a == 3:
            usun_zadanie()
        if a == 4:
            zapisz_do_pliku()
        if a == 5:
            exit

        
   
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Zapisz zmiany do pliku")
        print("5. Wyjdź")

        a=int(input("co chcesz zrobić?"))
main()

    
    
