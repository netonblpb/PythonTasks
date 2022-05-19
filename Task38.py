#38 Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Входные данные:
#  'ываабв лповап абвцукв алоабвабв ываываыв'

# Выходные данные: 
# 'лповап ываываыв'


EnterString = input('Введите строку: ')
StringArray = EnterString.split(' ')
DelString = 'абв'
FinalString = ''

for i in range (0, len(StringArray)):
    if DelString not in StringArray[i]:
        FinalString += StringArray[i] + ' '

print(FinalString)