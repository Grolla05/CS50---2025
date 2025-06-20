#include <cs50.h>
#include <stdio.h>

void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("Meow\n");
    }
}

int main(void)
{
    int n = 0;
    do
    {
        n = get_int("Numero: ");
    }
    while (n < 1);
    meow(n);
}
