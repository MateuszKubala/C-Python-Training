def main():
    for a in range(1, 1333):  
        for b in range(1, 1333):  
            c = a * a
            d = b * b
            e = str(a) + str(b)
            f = int(e)
            g = c + d
            

            if f == g:
                print("Wynik: ", f, "=", g)


main()
