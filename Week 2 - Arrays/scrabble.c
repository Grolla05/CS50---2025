#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Array com os pontos para cada letra de A a Z
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

// Protótipo da função que calcula a pontuação
int compute_score(string word);

int main(void)
{
    // 1. Pede a palavra de cada jogador
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // 2. Calcula a pontuação para cada palavra
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // 3. Compara as pontuações e imprime o vencedor
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    int score = 0;

    // Itera sobre cada caractere da palavra
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        // Verifica se o caractere é uma letra do alfabeto
        if (isalpha(word[i]))
        {
            // Converte a letra para maiúscula para padronizar
            char upper_char = toupper(word[i]);
            // Calcula o índice (0-25) e adiciona os pontos ao placar
            score += POINTS[upper_char - 'A'];
        }
    }

    return score;
}
