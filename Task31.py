# 31.	Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

numb = int(input('Введите число: '))

# div = 2

# while div < numb / 2 + 1:
#     prime = 1
#     if numb % div == 0:
#         prime = 0
#         for i in range (2, div):
#             if div % i == 0:
#                 prime = 1
#     if prime == 0: 
#         print(div)
#     div += 1


N = int(input("Введите натуральное число N:\n"))
List = []
for i in range(2, N):
    while N % i == 0:
        List.append(i)
        N = N/i
    if N == 1:
        break

if len(List) == 0:
    print("Число является простым")
else:
    print("Cписок множителей числа N:")
    print(List)
