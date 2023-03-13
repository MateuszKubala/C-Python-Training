#include<cs50.h>
#include<stdio.h>

int srednia(int dlugosc, int tablica[]);
int main(void)

{
    int n = get_int("podaj zakres: ");
    int tablica[n];
    for (int i=0; i<n; i++)

    {
        tablica[i] = get_int("podaj wartość: \n");
    }
    printf("średnia: %i", srednia(n, tablica));
}
int srednia(int dlugosc, int tablica[])


{
    int suma=0;
    for (int i=0; i<dlugosc; i++)
    {
        suma += tablica[i];

    }
    return (float)suma / (float)dlugosc;



}