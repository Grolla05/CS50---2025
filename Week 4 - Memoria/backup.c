#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    printf("%i\n", *p);

    //Definicao de uma string a partir do conteudo de uma variavel char
    char *s = "HI!";
    /*
    printf("\n\n%c\n", s[0]);
    printf("%c\n", s[1]);
    printf("%c\n", s[2]);
    */
   //Maneira mais elegante de se fazer
    printf("\n\n%c\n", *s);
    printf("%c\n", *(s + 1));
    printf("%c\n", *(s + 2));
}
