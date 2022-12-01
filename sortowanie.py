def sortowanie(liczby):
    
    for i in range (len(liczby) - 1, 0, -1):
        for j in range (i):
            if liczby[j] > liczby [j+1]:
                liczby[j], liczby[j + 1] = liczby[j + 1], liczby[j]

def main():

    liczby = [2, 1, 99, 10, 3, 4]
    print()
    sortowanie(liczby)
    print(liczby)

main()
    
