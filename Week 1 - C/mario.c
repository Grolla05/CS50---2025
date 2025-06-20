#include <cs50.h>
#include <stdio.h>

// A função agora recebe a quantidade de blocos para esta linha E a altura total
void print_row(int bricks, int total_height)
{
    // 1. Calcula e imprime os espaços necessários
    int spaces = total_height - bricks;
    for (int j = 0; j < spaces; j++)
    {
        printf(" ");
    }

    // 2. Imprime a quantidade de blocos para esta linha
    for (int i = 0; i < bricks; i++)
    {
        printf("#");
    }

    // 3. Pula para a próxima linha
    printf("\n");
}

int main(void)
{
    int altura;
    do
    {
        altura = get_int("Qual altura da piramide voce deseja: ");
    }
    while (altura < 1 || altura > 8);

    // Itera sobre cada linha
    for (int i = 0; i < altura; i++)
    {
        // Chama a função para imprimir UMA linha, passando
        // o número de blocos (i + 1) e a altura total.
        print_row(i + 1, altura);
    }
}
