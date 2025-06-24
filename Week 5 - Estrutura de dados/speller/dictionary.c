// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h" // <-- ESTA LINHA É ESSENCIAL E DEVE VIR AQUI

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1]; // Agora o compilador sabe o que é LENGTH
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Variável para contar o número de palavras no dicionário
unsigned int word_counter = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // 1. Obtém o índice da tabela hash para a palavra
    unsigned int index = hash(word);

    // 2. Cria um ponteiro "cursor" para percorrer a lista ligada
    node *cursor = table[index];

    // 3. Percorre a lista ligada até o final
    while (cursor != NULL)
    {
        // 4. Compara a palavra (ignorando maiúsculas/minúsculas)
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true; // Palavra encontrada
        }
        // Move o cursor para o próximo nó
        cursor = cursor->next;
    }

    // Se o loop terminar, a palavra não foi encontrada
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Uma função de hash um pouco melhor que a original.
    // Soma os valores ASCII das letras (em minúsculo) e usa o resto da divisão por N.
    unsigned long total = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        total += tolower(word[i]);
    }
    return total % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // 1. Abrir o arquivo do dicionário
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false; // Não foi possível abrir o arquivo
    }

    // Buffer para ler cada palavra
    char word_buffer[LENGTH + 1];

    // 2. Ler cada palavra do arquivo até o final (EOF)
    while (fscanf(file, "%s", word_buffer) != EOF)
    {
        // 3. Criar um novo nó para cada palavra
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(file);
            return false; // Erro de alocação de memória
        }
        strcpy(new_node->word, word_buffer);
        new_node->next = NULL;

        // 4. Obter o índice da tabela hash para a palavra
        unsigned int index = hash(word_buffer);

        // 5. Inserir o nó na tabela hash (no início da lista ligada)
        new_node->next = table[index];
        table[index] = new_node;

        // 6. Incrementar o contador de palavras
        word_counter++;
    }

    // 7. Fechar o arquivo e retornar sucesso
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // 1. Itera sobre todos os "baldes" da tabela hash
    for (int i = 0; i < N; i++)
    {
        // Cria um cursor para o início de cada lista ligada
        node *cursor = table[i];

        // 2. Percorre a lista ligada até o final
        while (cursor != NULL)
        {
            // Usa um ponteiro temporário para não perder a referência do próximo nó
            node *tmp = cursor->next;
            // Libera o nó atual
            free(cursor);
            // Move o cursor para o próximo nó
            cursor = tmp;
        }
    }
    return true;
}
