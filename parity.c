#include<cs50.h>
#include<stdio.h>

int main(void)

{

    int n = get_int("n: ");
    int wynik = n % 2;
    printf("reszta: %i", wynik);
    if (wynik == 0)
        printf("parzysta");
    else if (wynik > 0)
        printf("nieparzysta");
}
