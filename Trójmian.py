import math

def pierwiastki(a, b, c):
    if a == 0:
        print("Błąd: a nie może być równe 0.")
        exit()
    else:
        delta = b * b - 4 * a * c
        
    if delta < 0:
        print("Brak rozwiązań.")
    elif delta == 0:
        x1 = -b / (2 * a)
        print("x1 = ", x1)
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("x1 = ", x1, "x2 = ", x2)

def main():
    pierwiastki(1, 5, 4)

main()
