# Подсчитать сумму цифр в вещественном числе.

numb = input('Введите вещественное число: ')
summa = 0

numb = numb.replace('.', '')

# -----------  Вариант 1 -----------------
# for i in numb:
#     summa = summa + int(i)

# -----------  Вариант 2 -----------------
summa = sum(map(int, str(numb)))

print(summa)