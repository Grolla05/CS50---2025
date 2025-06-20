#include <cs50.h>
#include <stdio.h>

// O arranjo feito neste programa, mostra que ao executar digitando o nome o próprio software já
// preenche Por exemplo executando ./greet Felipe, o programa cairá no primeiro if do software e
// exportar "Ola, Felipe"

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        printf("Ola, %s\n", argv[1]);
    }
    else
    {
        printf("Ola, mundo\n");
    }
}
