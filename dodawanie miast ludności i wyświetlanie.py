countries_information = {}
file=open("countries", "w+")
def dodajkraje(countries_information):
 
    countries_information["PL"] = ("Wwa", 2231)
    countries_information["DE"] = ("Brln", 123532)
    countries_information["FR"] = ("Paris", 46534)
    stolica=input("Miasto: ")
    mieszkancy=int(input("Podaj liczbę: "))
    kraj=input("kraj: ")
    countries_information[kraj] = (stolica, mieszkancy)
    nowy=input("chcesz dodac nowy kraj? (t/n)")
    if nowy=="t":
        print("dodaj kolejny kraj")
        return(dodajkraje(countries_information))

dodajkraje(countries_information)

def show_country_info(country):
        country_information=countries_information.get(country)
        print()
        print(country)
        print("-----")
        print("stolica: ", country)
        print("liczba mieszkancow: ", country_information[1])


for country in countries_information.keys():
        print("LISTA:", country)

country = input("jaki kraj: ")
show_country_info(country)

for country, capitals in countries_information.items():
    file.write(country + " " + capitals)
file.close()
