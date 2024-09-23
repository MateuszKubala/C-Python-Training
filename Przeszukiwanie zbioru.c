#include <stdio.h>
#include <string.h>

typedef struct
{
    char name[50];   
    char number[15]; 
} person;

int main(void)
{
    person people[4];

    // Inicjalizacja danych
    strcpy(people[0].name, "janusz");
    strcpy(people[0].number, "124324");

    strcpy(people[1].name, "grzegorz");
    strcpy(people[1].number, "1214323244");

    strcpy(people[2].name, "mariusz");
    strcpy(people[2].number, "1212314324");

    strcpy(people[3].name, "piotr");
    strcpy(people[3].number, "12411324");

    // Wyszukiwanie osoby
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(people[i].name, "grzegorz") == 0)
        {
            printf("Jest, %s\n", people[i].number);
            return 0;
        }
    }
    
    printf("Nie\n");
    return 1;
}
