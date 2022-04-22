#Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]


def recprod(index):
    if index == 1: 
        print(f'1', end=' ')
        return 1
    else: 
        s = index * recprod(index - 1)
        print(f'{s}', end=' ')
        return s

ind = 7

recprod(ind)