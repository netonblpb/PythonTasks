# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

collection = '1 45 655 23 165 13 8'
splitted = collection.split()
min = int(collection[0])
max = int(collection[0])

for i in range(0, len(splitted)):
    if int(splitted[i]) > max: max = int(splitted[i])
    if int(splitted[i]) < min: min = int(splitted[i])

print(f'{min}       {max}')