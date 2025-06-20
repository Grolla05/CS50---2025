import sys

# Verifica se o sistema foi inicializado com passagem de parametro, caso nao tenha sido mensagem de erro
if len(sys.argv) != 2:
    print("Missing command-line argument")
    # Fecha o software logo apos imprimir a mensagem de erro
    sys.exit(1)

# Caso tenha sido imprime a mensagem de Hello parametro escrito, provavelmente o nome do usuario
print(f"Hello, {sys.argv[1]}")
# Fecha o software logo apos imprimir a mensagem de Hello, argumento
sys.exit(0)

# OBS: Caso seja executado o comando echo$? e possivel ver o valor retornado de sys.exit
# ou seja, no primeiro caso sem passagem de parametro sera observado o retorno como 1
# ja no outro caso o outrput do retorno sera 0
