#2.	Найти максимальное из пяти чисел

numbers = [1, 34, 2, 4, 7]

print(numbers)
maximum = numbers[0]

for i in numbers:
    if i > maximum:
        maximum = i

print(maximum)

#простой способ
print(max(numbers))