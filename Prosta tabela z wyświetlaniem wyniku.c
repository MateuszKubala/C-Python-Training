#include <stdio.h>

int main(void)
{
    // Deklaracja tablicy
    char *tabela[4];

    // Wartości do tablicy
    tabela[0] = "xxxxx";
    tabela[1] = "yyyyy";
    tabela[2] = "zzzzz";
    tabela[3] = "aaaaa";

    // Wyświetlenie czwartego elementu tablicy
    printf("%s\n", tabela[3]);

    return 0;
}
