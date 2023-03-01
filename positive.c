#include<cs50.h>
#include<stdio.h>

int get_positive_int(void);

int main(void)
{
    int i = get_positive_int();
    printf("sad%i\n",i);
}
int get_positive_int(void)
{
    int n;
    do
    {
            n = get_int("integer: ");
    }
    while(n<1);
    return n;
}
