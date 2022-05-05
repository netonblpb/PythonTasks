# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5.0, 10.03]
divlist = []

for i in list:
    divlist.append(round(i%1, 10))

print(divlist)

max = 0

for i in range(0, len(divlist)) :
    for j in range(0, len(divlist)):
        modul = abs(divlist[i] - divlist[j])
        if divlist[j] != 0 and divlist[i] != 0 and modul > max:
            max = modul

print(max)