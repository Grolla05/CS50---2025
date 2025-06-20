from sys import argv

## inicializacao do sistema com python greet.py nome
if len(argv) == 2:
    print(f"Hello, {argv[1]}")

else:
    print("Hello, World")
