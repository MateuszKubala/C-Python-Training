#include <stdio.h>

float average(int length, int array[]);

int main(void)
{
    int n;
    printf("Rozmiar tablicy: ");
    scanf("%d", &n);  

    int rekord[n];  // Deklaracja tablicy o rozmiarze n
    for (int i = 0; i < n; i++)
    {
        printf("Wynik %i: ", i + 1);
        scanf("%d", &rekord[i]);  // Pobranie wartości do tablicy
    }

    printf("Średnia: %.2f\n", average(n, rekord)); 
    return 0;  
}

float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];  
    }
    return (float)sum / length;  
}
