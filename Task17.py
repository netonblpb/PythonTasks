# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

dots = int(input('Введите значение для крайних точек: '))

elements = []
mult = 1
f = open('File.txt', 'r')

for i in range (-dots, dots + 1):
    elements.append(i)

print(elements)

for line in f:
    mult = mult * int(elements[int(line)])

print(mult)
