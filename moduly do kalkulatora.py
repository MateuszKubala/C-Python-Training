from kalkulator import*

def main():
    
    x=int(input("1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie"))
    a=float(input("podaj a: "))
    b=float(input("podaj b: "))

    if x==1:
        print(dodawanie(a,b))
        if x==2:
            print(odejmowanie(a,b))
            if x==3:
                print(mnozenie(a,b))
                if x==4:
                    print(dzielenie(a,b))
          
main()
