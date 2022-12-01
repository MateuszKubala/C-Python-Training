import math

def main():

    for i in range(1000, 10000,1):
        a=i//100
        b=i%100
        c=a*a+b*b
        if c==i:
            print("sa",c,"+",i)
        

main()
