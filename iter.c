#include<stdio.h>
#include<cs50.h>
#include<string.h>

void draw(int h);
int main(void)

{
    int height = get_int(" SAD: ");
    draw (height);
}

void draw(int h)
{
    for (int i=4; i>=0; i=i-1)
    {
        for (int j=0; j<=i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}