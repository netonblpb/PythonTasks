# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

dots = int(input('Введите значение для крайних точек: '))

elements = []
mult = 1
file = open('File.txt', 'r')

# -----------  Вариант 1 -----------------
# for i in range (-dots, dots + 1):
#     elements.append(i)

# print(elements)

# for line in file:
#     mult = mult * int(elements[int(line)])

# print(mult)

# -----------  Вариант 2 -----------------
elements = [i for i in range (-dots, dots + 1)]

for line in file:
    mult = mult * int(elements[int(line)])

print(elements)
print(mult)

file.close()