# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

count = int(input('Введите количество элементов: '))
num = 1
list = [1]

for i in range (0, count - 1):
    num *= -3
    list.append(num)

print(list)