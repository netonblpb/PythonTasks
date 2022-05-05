# Найти сумму чисел списка стоящих на нечетной позиции

list = [1, 2, 3, 2, 4, 2, 6, 2]
summ = 0

for i in range (len(list)):
    if i % 2 == 0:
        summ += list[i]

print(summ)
