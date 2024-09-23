import math

def main():

    for liczbypierwsze in range (2, 150):
        if all (liczbypierwsze%i !=0 for i in range(2,int(math.sqrt(liczbypierwsze)))):
            print(liczbypierwsze)




main()
