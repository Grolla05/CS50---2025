# Loop para garantir que a entrada do usuário seja válida
while True:
    try:
        # Pede a entrada do usuário (pode ser um valor como 0.41)
        dollars = float(input("Change owed: "))
        # Se o valor for não negativo, podemos prosseguir
        if dollars >= 0:
            break
    except ValueError:
        # Se a entrada não for um número, o loop continua, pedindo novamente
        pass

# Converte o valor em dólares para centavos, arredondando para evitar erros de ponto flutuante
cents = round(dollars * 100)

# Variável para contar o número total de moedas
coins = 0

# 1. Calcula a quantidade de moedas de 25 centavos (quarters)
coins += cents // 25
cents %= 25

# 2. Calcula a quantidade de moedas de 10 centavos (dimes)
coins += cents // 10
cents %= 10

# 3. Calcula a quantidade de moedas de 5 centavos (nickels)
coins += cents // 5
cents %= 5

# 4. O restante são as moedas de 1 centavo (pennies)
coins += cents

# 5. Imprime o número total de moedas
print(coins)
