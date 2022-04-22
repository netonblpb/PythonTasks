# Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму

amount = int(input('Введите количество элементов последовательности: '))
summa = 0

for i in range(1, amount):    
    summa = summa + ((1 + 1 / i) ** i)

print(summa)