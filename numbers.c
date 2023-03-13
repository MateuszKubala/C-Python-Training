#include<stdio.h>
#include<cs50.h>
#include<string.h>

int main(void)

{
    string tabela[6] = {"grzegorz", "janusz", "jerzy", "wojciech", "mariusz", "piotr"};
    string numery[6] = {"2343242", "234521", "8284324", "3211121", "41231311", "1212"};

    for (int i= 0; i<6; i++)
    {
        if (strcmp(tabela[i], "jerzy") == 0)
        {
            printf("%s", numery[i]);
            return 0;
        }
    }
    printf("nie");
    return 1;

}