import math

    

def pierwiastki(a, b, c):
    
    if a==0:
        print("brak")
        exit()
    else:
        delta=b*b-4*a*c
        
    if delta < 0:
        print("brak")
    elif delta == 0:
        x1=-b-(2*a)
        print(x1)
    else:
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
    print("x1 = ", x1, "x2 = ", x2)
    pierwiastki()

def main():
    pierwiastki(1, 5, 4)
main()
