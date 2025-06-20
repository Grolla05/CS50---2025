# Pede ao usuário uma altura até que uma entrada válida (um inteiro entre 1 e 8) seja fornecida
while True:
    try:
        # Pede a entrada do usuário
        height = int(input("Height: "))
        # Verifica se o número está no intervalo válido
        if 1 <= height <= 8:
            break  # Sai do loop se a entrada for válida
    except ValueError:
        # Se a entrada não for um número inteiro, o loop continua, pedindo novamente
        pass

# Itera de 1 até a altura fornecida (inclusive)
for i in range(1, height + 1):
    # Calcula o número de espaços e de hashes para a linha atual
    spaces = height - i
    hashes = i

    # Imprime os espaços seguidos pelos hashes para formar a pirâmide alinhada à direita
    print(" " * spaces + "#" * hashes)
