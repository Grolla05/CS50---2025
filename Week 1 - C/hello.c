# include <cs50.h>
# include <stdio.h>

int main (void)
{
    string answer = get_string("Qual é seu nome? ");
    printf("Hello, %s\n", answer);
}
