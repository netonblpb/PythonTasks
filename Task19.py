import time

x = time.time()
timespot = str(x)
ran = ''
expo = int(input('Введите количество знаков в нужном Вам случайном числе: '))

print(x)
for i in range (-expo, 0):
    ran = ran + timespot[i]
print(ran)