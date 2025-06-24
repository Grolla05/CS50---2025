# 1. Pede o texto ao usuário
text = input("Text: ")

# 2. Inicializa os contadores
letters = 0
words = 1  # Começa em 1 para contar a última palavra que não é seguida de espaço
sentences = 0

# Itera sobre cada caractere do texto
for char in text:
    # Conta as letras (se o caractere for alfabético)
    if char.isalpha():
        letters += 1
    # Conta as palavras (se o caractere for um espaço)
    elif char == ' ':
        words += 1
    # Conta as sentenças (se o caractere for um ponto final, exclamação ou interrogação)
    elif char in ['.', '!', '?']:
        sentences += 1

# 3. Calcula L e S
# Em Python, a divisão / já resulta em float, então o casting não é necessário
L = (letters / words) * 100
S = (sentences / words) * 100

# Calcula o índice Coleman-Liau
index = 0.0588 * L - 0.296 * S - 15.8

# Arredonda o índice para o inteiro mais próximo
grade = round(index)

# 4. Imprime o resultado final de acordo com as regras
if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    # Usando f-string para uma formatação mais limpa
    print(f"Grade {grade}")
