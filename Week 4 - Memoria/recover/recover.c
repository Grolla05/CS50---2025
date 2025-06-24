#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Define o tamanho do bloco a ser lido do cartão
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // 1. Verifica se o usuário forneceu exatamente um argumento de linha de comando
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // 2. Abre o arquivo do cartão de memória para leitura
    FILE *raw_file = fopen(argv[1], "r");
    if (raw_file == NULL)
    {
        printf("Could not open file %s.\n", argv[1]);
        return 1;
    }

    // Declaração de variáveis
    unsigned char buffer[BLOCK_SIZE]; // Buffer para armazenar cada bloco de 512 bytes
    int file_counter = 0;             // Contador para os nomes dos arquivos JPEG
    FILE *img = NULL;                 // Ponteiro para o arquivo de imagem de saída
    char filename[8];                 // String para armazenar o nome do arquivo (ex: "000.jpg\0")

    // 3. Lê o arquivo do cartão de memória bloco por bloco
    while (fread(buffer, 1, BLOCK_SIZE, raw_file) == BLOCK_SIZE)
    {
        // 4. Verifica se o bloco atual é o início de um novo JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            // Se um JPEG já estava aberto, fecha-o primeiro
            if (img != NULL)
            {
                fclose(img);
            }

            // Cria o nome para o novo arquivo JPEG (ex: 000.jpg, 001.jpg, ...)
            sprintf(filename, "%03i.jpg", file_counter);
            // Abre o novo arquivo JPEG para escrita
            img = fopen(filename, "w");
            // Incrementa o contador de arquivos
            file_counter++;
        }

        // Se um arquivo JPEG já estiver aberto, continua a escrever nele
        if (img != NULL)
        {
            fwrite(buffer, 1, BLOCK_SIZE, img);
        }
    }

    // 6. Fecha os arquivos restantes no final do programa
    if (img != NULL)
    {
        fclose(img);
    }
    fclose(raw_file);

    return 0;
}
