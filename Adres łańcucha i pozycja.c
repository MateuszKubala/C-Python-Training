#include<stdio.h>
#include<string.h>

int main(void)
{
    char *i = "Mateusz";

    printf("Adres pamięci: %p\n", i);
    printf("Pierwszy znak: %c\n", i[0]);

    return 0;
}
