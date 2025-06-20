#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *a = get_string("a: ");
    char *b = get_string("b: ");

    printf("%p\n",a);
    printf("%p\n",b);

    if (strcmp(a, b)== 0)
    {
        printf("Igual\n");
    }
    else
    {
        printf("Diferente\n");
    }
}
