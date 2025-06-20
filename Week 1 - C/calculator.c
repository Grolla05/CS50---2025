#include <cs50.h>
#include <stdio.h>

// Este programa foi feito para mostrar na aula a presença de OVERFLOWS, estourar a quantidade de bits suportados pela memória da variável definida

int main(void){
    int dollars = 1;
    while(true){
        char c = get_char("Aqui tem $%i. Quer dobrar? \nOBS: responda somente com y ou n \nResposta: ", dollars);
        if(c== 'y'){
            dollars *=2;
        }
        else{
            break;
        }
    }
    printf("Aqui tem $%i.\n",dollars);
}
