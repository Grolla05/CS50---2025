#include <cs50.h>
#include <stdio.h>

int main (void){
    char c = get_char("Você aceita? ");
    if (c == 'y' || c == 'Y'){
        printf("Você aceitou!!!\n");
    }
    else if (c == 'n' || c == 'N'){
        printf("Você negou :(\n");
    }
    else{
        printf("Erro...\n");
    }
}
