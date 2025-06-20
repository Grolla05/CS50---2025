# names - ["Yuliia", "David", "John"]
#
# name = input("Nome: ")

# for n in names:
#    if name == n:
#        print("Encontrado")
#        break
#
#   else:
#        print("Nao Encontrado)

# if name in names:
#    print("Encontrado")

# else:
#   print("Nao Encontrado")

# Estruturacao do que seria o banco do sistema
# people = [
#    {"name": "Yuliia","number": "+1-617-495-1000"},
#    {"name": "David", "number": "+1-617-495-999"},
#    {"name": "John", "number": "+1-949-468-2750"}
# ]

# Inserir o nome desejado para mbusca do numero
# name = input("Nome: ")
# Parte logica do sistema onde dentro do banco sera buscado o nome desejado
# for person in people:
#    if person["name"] == name:
#       number = person["number"]
#        print(f"Encontrado {number}")
#        break
#
# else:
#    print("Nao Encontrado")


people = {
    "Yuliia": "+1-617-495-1000",
    "David": "+1-617-495-1000",
    "John": "+1-949-468-2750",
}

name = input("Name: ")

if name in people:
    print(f"Number: {people[name]}")

else:
    print("Nao encontrado")
