#include<cs50.h>
#include<stdio.h>

int main(void)

{
    float price = get_float("jaka cena?");
    printf("cena z podatkiem: %.3f", price * 1.0625);
}
