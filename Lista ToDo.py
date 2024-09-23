lista_zadan = []

# Wyświetlanie zadań
def wyswietlanie():
    print("\nAktualna lista zadań:")
    if lista_zadan:
        for indeks, zadanie in enumerate(lista_zadan):
            print(f"Indeks: {indeks} | Treść: {zadanie}")
    else:
        print("Brak zadań na liście.")
    print()

# Dodawanie nowego zadania
def nowe_zadanie():
    print()
    nowe = input("Podaj treść nowego zadania: ").strip()
    if nowe:
        lista_zadan.append(nowe)
        print(f"Zadanie '{nowe}' zostało dodane.")
    else:
        print("Nie można dodać pustego zadania.")
    print()

# Usuwanie zadania
def usun_zadanie():
    print("\nPodaj numer zadania do usunięcia (od 0 do", len(lista_zadan) - 1, "):")
    wyswietlanie()
    
    try:
        indeks = int(input("Podaj indeks: "))
        if 0 <= indeks < len(lista_zadan):
            usuniete = lista_zadan.pop(indeks)
            print(f"Zadanie '{usuniete}' zostało usunięte.")
        else:
            print("Nie znaleziono zadania o podanym indeksie.")
    except ValueError:
        print("Podano nieprawidłowy numer. Proszę spróbować ponownie.")
    print()

# Zapisywanie zadań do pliku
def zapisz_do_pliku():
    with open("todo.txt", "w", encoding="utf-8") as file:
        for zadanie in lista_zadan:
            file.write(zadanie + "\n")
    print("\nZapisano zadania do pliku 'todo.txt'.\n")

# Wczytywanie zadań z pliku
def wczytywanie():
    try:
        with open("todo.txt", "r", encoding="utf-8") as file:
            for zadanie in file.readlines():
                lista_zadan.append(zadanie.strip())
        print("\nLista zadań została wczytana z pliku.\n")
    except FileNotFoundError:
        print("\nPlik 'todo.txt' nie istnieje. Utworzono nową listę.\n")

# Menu
def main():
    wczytywanie()
    
    opcja = None
    while opcja != 5:
        print("\nMenu:")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Zapisz zmiany do pliku")
        print("5. Wyjdź")

        try:
            opcja = int(input("Co chcesz zrobić? Wybierz opcję (1-5): "))
            
            if opcja == 1:
                wyswietlanie()
            elif opcja == 2:
                nowe_zadanie()
            elif opcja == 3:
                usun_zadanie()
            elif opcja == 4:
                zapisz_do_pliku()
            elif opcja == 5:
                print("Zakończono program.")
            else:
                print("Nieprawidłowa opcja. Wybierz liczbę od 1 do 5.")
        
        except ValueError:
            print("Nieprawidłowy wybór. Wprowadź liczbę od 1 do 5.")

if __name__ == "__main__":
    main()
