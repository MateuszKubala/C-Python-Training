def oblicz(a):

    return a*a+1
    
def main():

    f = float(input("podaj krok: "))
    krok = f
    x=0

    while x <= 5:
        y = oblicz(x)
        print("x = ", x,"y = ", y)
        x+= krok


    
main()
