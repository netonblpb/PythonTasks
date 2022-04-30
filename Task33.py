# Задана натуральная степень k. 
# Cформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

exp = 2
klist=[]
polynomial = ''

for i in range (0, exp + 1):
    klist.append(randint(1, 101))

print(klist)
file = open('Poly.txt', 'w')

for i in range (exp, -1, -1):
    if i > 1:
        polynomial += str(klist[-(i + 1)]) + ' * x ^ ' + str(i) + ' + '
    elif i == 1:
        polynomial += str(klist[-(i + 1)]) + ' * x + '
    elif i == 0:
        polynomial += str(klist[-(i + 1)]) + ' = 0'

print(polynomial)

file.write(polynomial)
file.close