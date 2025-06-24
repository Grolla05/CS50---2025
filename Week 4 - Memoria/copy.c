#include <cs50.h> //Get_string()
#include <ctype.h> //Toupper()
#include <stdio.h> //Printf()
#include <stdlib.h> //malloc e free
#include <string.h> // strlen() e strcpy()

int main(void)
{
    char *s = get_string("s:");
    char *t = malloc(strlen(s) + 1); // mais um por conta do caractere NULL

    if (t == NULL)
    {
        return 1;
    }

    strcpy(t, s);

    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    printf("s: %s\n", s);
    printf("t: %s\n", t);

    free(t);
}
