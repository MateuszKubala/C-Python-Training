import math

def main():

    for i in range(1000, 10000,1):
        a=i//100    #pierwsze dwie cyfry
        b=i%100     #ostatnie dwie cyfry
        c=a*a+b*b
        if c==i:
            print(f"{i} spełnia warunek: {a}^2 + {b}^2 = {i}")
        

main()
