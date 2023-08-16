#1) Ler o arquivo "actors.csv" (disponível no Google Classroom)  por meio de código em Python, usando o pacote "csv".
#2) Retirar o cabeçalho do arquivo lido.

import csv

with open('actors.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        print(line)




