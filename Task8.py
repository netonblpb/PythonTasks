# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 

X = int(input('Введите координату Х:'))
Y = int(input('Введите координату Y:'))

if (X == 0 and Y == 0):
    print(f'Точка {X},{Y} находится в начале координат')
if (X == 0 and Y != 0):
    print(f'Точка {X},{Y} находится на оси Х')
if (X != 0 and Y == 0):
    print(f'Точка {X},{Y} находится на оси Y')
if (X > 0 and Y > 0):
    print(f'Точка {X},{Y} находится в первой четверти')
if (X < 0 and Y > 0):
    print(f'Точка {X},{Y} находится во второй четверти')
if (X < 0 and Y < 0):
    print(f'Точка {X},{Y} находится в третьей четверти')
if (X > 0 and Y < 0):
    print(f'Точка {X},{Y} находится в четвертой четверти')