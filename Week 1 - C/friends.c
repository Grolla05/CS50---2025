#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Name
    string name = get_string("Qual e seu nome: ");

    // Age
    int idade = get_int("Qual e a sua idade: ");

    // Cidade
    string cidade = get_string("Qual e a sua cidade: ");

    // numero de celular
    int numero = get_int("Qual e seu numero de telefone: ");

    printf("nome: %s \nidade: %i \ncidade: %s \ntelefone: %i \n", name, idade, cidade, numero);
}
