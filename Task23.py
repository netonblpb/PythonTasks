# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

numbers = [2, 3, 4, 5, 6, 7, 8]
mult = []

for i in range (0, int((len(numbers)-1)//2 + 1)):
    mult.append(numbers[i] * numbers[-i-1])

print(mult)