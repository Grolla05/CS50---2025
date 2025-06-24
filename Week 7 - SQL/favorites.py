import csv

# Leitura e print na tela de um determinado campo
with open("nome_do_arquivo_csv.csv", "r") as file:
    # Ao definir a lida do arquivo como dicionario fara com que as atribuições de qual campo deve ler / filtrar e etc
    # Seja pelo nome definido, como pode-se observar na linha 8
    reader = csv.DictReader(file)
    next(reader)
    for row in reader:
        # Definicao da variavel a partir da coluna denominada como language
        favorite = row["language"]
        print(favorite)
        # Tanto o de cima quanto o de baixo esta certo
        print(row["language"])
        # print(row[1])


# Contagem de dados
# Por exemplo quantas pessoas escolheram XX ou YY
# O exemplo apresentado abaixo se baseia em um csv no qual as pessoas escolhiam sua linguagem favorita
import csv

with open("nome_do_arquivo_csv.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        # favorites e definido pela linguagem na qual esta ssendo analisada daquela respectiva linha
        favorite = row["language"]
        if favorite in counts:
            # Soma 1 em counts[linguagem analisada]
            counts[favorite] += 1
        else:
            counts[favorites] = 1

# Print dos resultados na tela e imprime de maneira organizada alfabeticamente
for favorite in sorted(counts, key=counts.get, reverse=True):
    print(f"{favorite}: {counts[favorite]}")
