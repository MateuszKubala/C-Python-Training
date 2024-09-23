#include<stdio.h>

int main(int argc, char *argv[])
{
    if (argc == 2) // argc=licznik argumentów (1szy to nazwa programu, drugi to argv[1] itd.)
    {
        printf("hello, %s\n", argv[1]); // s% - wywołanie wskaźnika (z funkcji argv[1])
    }
    else
    {
        printf("hello, world\n");
    }

    return 0; 
}
