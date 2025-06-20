#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // 1. Pede o valor do troco ao usuário
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    // Variável para contar o número total de moedas
    int coins = 0;

    // 2. Calcula a quantidade de moedas de 25 centavos (quarters)
    coins += cents / 25;
    cents %= 25;

    // 3. Calcula a quantidade de moedas de 10 centavos (dimes)
    coins += cents / 10;
    cents %= 10;

    // 4. Calcula a quantidade de moedas de 5 centavos (nickels)
    coins += cents / 5;
    cents %= 5;

    // 5. O restante são as moedas de 1 centavo (pennies)
    coins += cents;

    // 6. Imprime o número total de moedas
    printf("%i\n", coins);
}
