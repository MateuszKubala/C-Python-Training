#include<stdio.h>
#include<cs50.h>


float average(int length, int array[]);

int main(void)
{
    int n = get_int("rozmiar tablicy: ");
    int rekord[n];
    for (int i=0; i<n; i++)
    {
        rekord[i]=get_int("score %i:", i+1);
    }
    printf("average : %1.f\n", average(n, rekore));
}

float average(int length, int array[])
{
    int sum = 0;
    for (int i=0; i<length; i++)
    {
        sum += array[i];
    }
    return sum / length;
}