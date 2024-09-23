#include <stdio.h>

float srednia(int dlugosc, int tablica[]);

int main(void)
{
    int n;
    printf("Podaj zakres: ");
    scanf("%d", &n);  

    int tablica[n];  
    for (int i = 0; i < n; i++)
    {
        printf("Podaj wartość %i: ", i + 1);
        scanf("%d", &tablica[i]);  
    }

    printf("Średnia: %.2f\n", srednia(n, tablica));  
    return 0;  
}

float srednia(int dlugosc, int tablica[])
{
    int suma = 0;
    for (int i = 0; i < dlugosc; i++)
    {
        suma += tablica[i];  
    }
    return (float)suma / dlugosc;  
}
