#include <cs50.h>
#include <stdio.h>
#include <string.h>

#define MAX 7

int main(void)
{
    string str[MAX] = {"battleship", "boot", "cannon", "iron", "thimble", "top hat"};
    string s = get_string("String: ");
    for (int i = 0; i < 6; i++)
    {
        if (strcmp(str[i], s))
        {
            printf("Encontrado\n");
            return 0;
        }
    }
    printf("Nao encontrado\n");
    return 1;
}
