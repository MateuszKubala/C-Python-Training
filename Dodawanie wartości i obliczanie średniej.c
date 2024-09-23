#include <stdio.h>

int srednia(int dlugosc, int tabela1[]);

int main(void)
{
    int n;
    printf("Podaj rozmiar tabeli: ");
    scanf("%d", &n); 

    int tabela[n];
    for (int i = 0; i < n; i++)
    {
        printf("Podaj wartosc: ");
        scanf("%d", &tabela[i]);  
    }

    printf("Srednia: %.2f\n", (float)srednia(n, tabela)); 
    return 0;
}

int srednia(int dlugosc, int tabela1[])
{
    int suma = 0;
    for (int i = 0; i < dlugosc; i++)
    {
        suma += tabela1[i];
    }
    return suma;  
}
