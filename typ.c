#include<stdio.h>
#include<cs50.h>
#include<string.h>


typedef struct
{
    string name;
    string number;
}
person;

int main(void)

{
    person people[4];
    people[0].name = "janusz";
    people[0].number = "124324";

    people[1].name = "grzegorz";
    people[1].number = "1214323244";

    people[2].name = "mariusz";
    people[2].number = "1212314324";

    people[3].name = "piotr";
    people[3].number = "12411324";

    for (int i=0; i<4; i++)
    if (strcmp(people[i].name, "grzegorz") == 0)
    {
        printf("jest, %s", people[i].number);
        return 0;

    }
    printf("nie");
    return 1;
}
