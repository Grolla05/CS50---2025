#include <cs50.h>
#include <stdio.h>

int main(void){
    int x = get_int("Insira o valor de X = ");
    int y = get_int("Insira o valor de Y = ");
    if(x < y){
        printf("X é menor que Y\n");
    }

    else if(x == y){
        printf("X é igual a Y\n");
    }

    else{
        printf("X é maior que Y\n");
    }
}
