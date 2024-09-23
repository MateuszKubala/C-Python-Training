#include <stdio.h>
#include <string.h>

int main(void)
{
    // Tablice z imionami i numerami
    char *tabela[6] = {"grzegorz", "janusz", "jerzy", "wojciech", "mariusz", "piotr"};
    char *numery[6] = {"2343242", "234521", "8284324", "3211121", "41231311", "1212"};

    // Wprowadzenia nazwiska do wyszukania
    char szukana_osoba[50]; // Przydzielenie pamięci dla wprowadzonego nazwiska
    printf("Podaj imię do wyszukania: ");
    scanf("%49s", szukana_osoba); // Ograniczenie długości wejścia

    for (int i = 0; i < 6; i++)
    {
        if (strcmp(tabela[i], szukana_osoba) == 0)
        {
            printf("Numer dla %s: %s\n", szukana_osoba, numery[i]);
            return 0; // Zakończenie programu po znalezieniu
        }
    }

    printf("Nie znaleziono numeru dla %s\n", szukana_osoba);
    return 1; // Zwrócenie błędu, gdy nie znaleziono
}
