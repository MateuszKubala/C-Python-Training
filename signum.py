import math

def signum(x):

    
    if x < 0:
        sig = -1
    if x == 0:
        sig = 0
    if x > 0:
        sig = 1
        
    print(sig)

def main():

        signum(0)
        signum(3)
        signum(-2)
        signum(-10)

main()
