def main():


    j=0
    for i in range(10000,1000000,1):
        a=i//1000
        b=i%1000
        c=a*a+b*b
        if c == i:
            print("super ", c,"=",i)
            j=j+1
            print("liczba =", j)
        




main()
