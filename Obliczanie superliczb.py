def main():
    # Zakres od użytkownika
    start = int(input("Podaj początkową wartość zakresu (min. 10000): "))
    end = int(input("Podaj końcową wartość zakresu (np. 999999): "))

    # Minimalna wartość
    if start < 10000:
        print("Początkowa wartość została ustawiona na 10000.")
        start = 10000

    j = 0
    for i in range(start, end + 1):
        a = i // 1000  # Pierwsze trzy cyfry liczby i, dzielenie całkowite
        b = i % 1000   # Ostatnie trzy cyfry, reszta z dzielenia
        c = a * a + b * b
        if c == i:
            print("Super liczba:", i, "=", c)
            j += 1
            print("a= ", a, " b= ", b, " c= ",c)

    print("Liczba super liczb:", j)

main()
