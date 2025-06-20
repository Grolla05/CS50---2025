#include <cs50.h>
#include <stdio.h>

void print_row(int bricks)
{
    for (int i = 0; i < bricks; i++)
    {
        printf("#");
    }
    printf("\n");
}

int main(void)
{
    int altura = 0;
    // qual altura da piramide o usuario quer
    do
    {
        altura = get_int("Qual altura da piramide voce deseja: ");
    }
    while (altura < 1);

    // printar a piramide com a altura solicitada
    for (int i = 0; i < altura; i++)
    {
        print_row(i + 1);
    }
}
