# Определить, присутствует ли в заданном списке строк, некоторое число 

from tokenize import Number


string1 = input('Введите строку: ')
number = int(input('введите число: '))
present = 0


if (string1.count(str(number))):
    print(f'Число {number} присутствует в заданной строке.')
else:
    print(f'Число {number} отсутствует в заданной строке.')
