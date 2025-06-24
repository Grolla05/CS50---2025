#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Protótipos das funções
bool only_digits(string s);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    // 1. Validar os argumentos de linha de comando
    // Verifica se foi passado exatamente um argumento e se ele contém apenas dígitos
    if (argc != 2 || !only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1; // Encerra com código de erro
    }

    // 2. Converter a chave (string) para um inteiro
    int key = atoi(argv[1]);

    // 3. Solicitar o texto a ser criptografado
    string plaintext = get_string("plaintext:  ");

    // Imprime o cabeçalho do texto cifrado
    printf("ciphertext: ");

    // 4. Percorrer o texto, rotacionar cada caractere e imprimir
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        char rotated_char = rotate(plaintext[i], key);
        printf("%c", rotated_char);
    }

    // Imprime a quebra de linha final
    printf("\n");
    return 0; // Encerra com sucesso
}

// Função para verificar se uma string contém apenas dígitos
bool only_digits(string s)
{
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}

// Função para rotacionar um único caractere pela chave 'n'
char rotate(char c, int n)
{
    // Se não for uma letra, retorna o caractere original
    if (!isalpha(c))
    {
        return c;
    }

    // Define a base ('A' para maiúsculas, 'a' para minúsculas)
    char base = isupper(c) ? 'A' : 'a';

    // Aplica a fórmula da Cifra de César
    return (c - base + n) % 26 + base;
}
