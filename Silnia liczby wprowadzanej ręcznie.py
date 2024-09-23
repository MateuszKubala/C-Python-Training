def main():
    n = int(input("Podaj wartość n: "))
    for x in range(n):
        silnia = 1  
        for y in range(1, x + 1):  
            silnia *= y
        print(f"Silnia {x} = {silnia}")  


main()
