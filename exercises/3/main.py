#3) Calcular automaticamente a média entre todas as idades dos artistas descritos no arquivo.

import csv
import datetime

def calculate_age(born):
    born = datetime.datetime.strptime(born, "%B %d, %Y")
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

items = 0;
ages_sum =0;
with open('actors.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        items += 1
        ages_sum += calculate_age(line[2])
print("A média de idades é: " + (ages_sum/items).__str__() + " anos")        






