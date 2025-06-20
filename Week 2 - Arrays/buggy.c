#include <cs50.h>
#include <stdio.h>

void print_column(int altura)
{
    for (int i = 0; i <= altura; i++)
    {
        printf("#\n");
    }
}

int main(void)
{
    int altura = get_int("Altura: ");
    print_column(altura);
}
