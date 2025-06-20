import csv
import sys


def main():

    # 1. Verifica se o uso na linha de comando está correto (python dna.py data.csv sequence.txt)
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # 2. Lê o arquivo do banco de dados (CSV) para a memória
    database = []
    # Abre o arquivo CSV e usa o DictReader para ler as linhas como dicionários
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        # A primeira linha (cabeçalho) nos dá os nomes dos STRs a serem verificados
        # reader.fieldnames é uma lista com os nomes das colunas. Ex: ['name', 'AGAT', 'AATG', 'TATC']
        # Pegamos todos, exceto o primeiro ('name'), que são os STRs
        strs_to_check = reader.fieldnames[1:]

        # Itera sobre cada linha (pessoa) do arquivo CSV
        for row in reader:
            # Converte os valores dos STRs de string para inteiro
            for str_name in strs_to_check:
                row[str_name] = int(row[str_name])
            # Adiciona a pessoa (como um dicionário) à nossa lista de banco de dados
            database.append(row)

    # 3. Lê o arquivo da sequência de DNA para a memória
    with open(sys.argv[2]) as file:
        dna_sequence = file.read()

    # 4. Encontra a maior sequência de cada STR na sequência de DNA
    # Cria um dicionário para armazenar os resultados (ex: {'AGAT': 4, 'AATG': 1, 'TATC': 5})
    calculated_strs = {}
    for str_name in strs_to_check:
        # Usa a função fornecida para encontrar a maior sequência
        longest = longest_match(dna_sequence, str_name)
        # Armazena o resultado no dicionário
        calculated_strs[str_name] = longest

    # 5. Verifica o banco de dados em busca de perfis correspondentes
    # Itera sobre cada pessoa no nosso banco de dados
    for person in database:
        match_count = 0
        # Para cada pessoa, itera sobre cada STR que precisamos verificar
        for str_name in strs_to_check:
            # Compara o valor do STR da pessoa no banco de dados com o valor que calculamos do DNA
            if person[str_name] == calculated_strs[str_name]:
                match_count += 1

        # Se o número de STRs correspondentes for igual ao total de STRs que verificamos...
        if match_count == len(strs_to_check):
            # ...encontramos uma correspondência! Imprime o nome e termina o programa.
            print(person["name"])
            return

    # Se o loop terminar e ninguém corresponder, imprime "No match"
    print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
