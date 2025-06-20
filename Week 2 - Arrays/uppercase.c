#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After: ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            printf("%c", toupper(s[i]));
        }
        else if (s[i] >= 'A' && s[i] <= 'Z'){
            printf("%c", s[i] + 32);
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
}
