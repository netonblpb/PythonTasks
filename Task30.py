# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001,π = 3.141             10^(-1)≤d≤10^(-10)

from cmath import pi

X = int(input('Введите количество знаков после запятой (1 - 10): ' ))
if (X < 1 or X > 10):
    print('Введенное число не соответствует заданному диапазону.')
else:
    print(f'pi = ', round(pi, X))