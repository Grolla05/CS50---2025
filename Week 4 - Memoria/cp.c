#include <stdint.h>
#include <stdio.h>

typedef uint8_t BYTE; // define BYTE como 8 bits

int main(int argc, char *argv[])
{
    FILE *src = fopen(argv[1], "r"); // abre o arquivo src em modo leitura
    FILE *dst = fopen(argv[2], "w"); // abre o arquivo dst em modo escrita

    BYTE b;

    while (fread(&b, sizeof(b), 1, src) != 0)
    {
        fwrite(&b, sizeof(b), 1, dst); // este loop funciona de modo no qual transcreve tudo de um
                                       // arquivo para outro automaticamente
    }

    fclose(dst);
    fclose(src);
}

// Quando rodar o comando deve ser ./cp ARQUIVO DE SRC.c ARQUIVO DE COPIA.c
