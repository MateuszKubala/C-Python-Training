file=open("countries.txt", "w+")
countries_information = {"Poland": "Warsaw",
                         "France": "Paris", "Germany": "Prague"}

for country, capitals in countries_information.items():
    file.write(country + "\t" + capitals + "\n")
file.close()
