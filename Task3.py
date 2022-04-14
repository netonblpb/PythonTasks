#3.	Вывести на экран числа от -N до N

num = -5

if num > 0:    
    for a in range(-num, num + 1):
        print(a)
elif num < 0:
    for a in range(-num, num - 1, -1):
        print(a)
