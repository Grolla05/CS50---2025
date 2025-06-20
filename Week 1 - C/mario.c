#include <cs50.h>
#include <stdio.h>

void print_row(int n)
{
    for (int c = 0; c < n; c++)
    {
        printf("#");
    }
    printf("\n");
}

int main(void)
{
    for (int r = 0; r < 3; r++)
    {
        print_row(3);
    }
}
