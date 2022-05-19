# 41.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: 
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные:
# 12W1B12W3B24W1B14W

proc = input('Выберите процесс (0 - ахивирование, 1 - восстановление): ')

if int(proc) == 0:
    result = ''
    count = 1
    string = input('Введите строку для архивирования: ')

    for i in range(0, len(string) - 1):        
        if i <= len(string) - 1:
            if string[i] == string[i+1]:
                count += 1
            else:
                result += str(count) + string[i]
                count = 1
        if i == len(string) - 2 and string[i] == string[i+1]:
            result += str(count) + string[i]
        if i == len(string) - 2 and string[i] != string[i+1]:
            result += str(count) + string[i]
            result += '1' + string[i+1]
    print(result)

numberInt = []
letterStr = []

if int(proc) == 1:
    string = input('Введите строку для восстановления: ')
    num = ''
    result = ''

    for i in range (0, len(string)):
        if string[i].isdigit():
            num += string[i]  
        if string[i].isalpha():
            numberInt.append(num)
            num = ''
            letterStr.append(string[i])
    
    for i in range (0, len(letterStr)):
        result += letterStr[i] * int(numberInt[i])

elif int(proc) != 0 and int(proc) != 1:
    print('Неверное условие!')

print(result)