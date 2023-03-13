#include<stdio.h>
#include<cs50.h>

int srednia(int dlugosc, int tabela1[]);
int main(void)

{
    int n = get_int("podaj rozmiar tabeli: ");
    int tabela[n];
    for (int i=0; i<n; i++)

    {
        tabela[i] = get_int("podaj wartosc: ");

    }
    printf("srednia: %i", srednia(n, tabela));
}

int srednia (int dlugosc, int tabela1[])
{
    int suma = 0;
    for (int i=0; i<dlugosc; i++)
    {
        suma += tabela1[i];
    }
    return suma / dlugosc;
}