#include <stdio.h> 
#include <string.h> 

void draw(int h);

int main(void)
{
    int height;

    // wysokość
    do
    {
        printf("Podaj wysokość piramidy: ");
        scanf("%d", &height);
    } while (height <= 0);

    draw(height);
}

void draw(int h)
{
    for (int i = h; i > 0; i--)
    {
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
