countries_information = {}

# Otwarcie pliku do zapisu i odczytu
file = open("countries.txt", "w+")

def dodaj_kraje(countries_information):
    # Dodanie wstępnych danych
    countries_information["PL"] = ("Warszawa", 2231000)
    countries_information["DE"] = ("Berlin", 3562000)
    countries_information["FR"] = ("Paryż", 2161000)
    
    while True:
        kraj = input("Podaj kod kraju (np. 'PL'): ").upper()
        stolica = input("Podaj stolicę: ")
        mieszkancy = int(input("Podaj liczbę mieszkańców: "))

        countries_information[kraj] = (stolica, mieszkancy)
        
        nowy = input("Czy chcesz dodać nowy kraj? (t/n): ").lower()
        if nowy != "t":
            break

def show_country_info(country):
    country_information = countries_information.get(country.upper())
    
    if country_information:
        print(f"\nInformacje o kraju: {country}")
        print("--------------------------")
        print(f"Stolica: {country_information[0]}")
        print(f"Liczba mieszkańców: {country_information[1]}")
    else:
        print("Nie znaleziono informacji o podanym kraju.")

# Funkcja do zapisywania danych do pliku
def zapisz_do_pliku(countries_information):
    for country, info in countries_information.items():
        file.write(f"{country} {info[0]} {info[1]}\n")

dodaj_kraje(countries_information)

# Wyświetlanie listy dostępnych krajów
print("\nLista krajów:")
for country in countries_information.keys():
    print("- ", country)

country = input("\nPodaj kod kraju, którego informacje chcesz zobaczyć: ")
show_country_info(country)

# Zapisywanie danych do pliku
zapisz_do_pliku(countries_information)

# Zamknięcie pliku
file.close()
print("\nDane zostały zapisane do pliku 'countries.txt'.")
