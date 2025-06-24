#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // 1. Pede o texto ao usuário
    string text = get_string("Text: ");

    // 2. Inicializa os contadores
    int letters = 0;
    int words = 1; // Começa em 1 porque a última palavra não tem espaço depois
    int sentences = 0;

    // Itera sobre o texto para contar letras, palavras e sentenças
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // Conta as letras
        if (isalpha(text[i]))
        {
            letters++;
        }
        // Conta as palavras (baseado nos espaços)
        else if (text[i] == ' ')
        {
            words++;
        }
        // Conta as sentenças
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
    }

    // 3. Calcula L e S (usando float para precisão)
    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;

    // Calcula o índice Coleman-Liau
    float index = 0.0588 * L - 0.296 * S - 15.8;

    // Arredonda o índice para o inteiro mais próximo
    int grade = round(index);

    // 4. Imprime o resultado final de acordo com as regras
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}
