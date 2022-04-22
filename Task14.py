# Подсчитать сумму цифр в вещественном числе.

numb = input('Введите вещественное число: ')
sum = 0

numb = numb.replace('.', '')

for i in numb:
    sum = sum + int(i)
print(sum)