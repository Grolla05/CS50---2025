import csv

#Inserir os valores a serem adicionados na planilha neste caso nome e numero
name = input("Name: ")
number = input("Number: ")

#Abre / cria o arquivo phonebook.csv
with open("phonebook.csv","a") as file:
    #Escreve os inputs solicitados na planilha de maneira automatica em ordem de fila
    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": number})
