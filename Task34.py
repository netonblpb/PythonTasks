# Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.

from unicodedata import decimal

# Создаём файлы и записываем в них многочлены

firstpoly = open('First.txt', 'w')
secondpoly = open('Second.txt', 'w')
poly1 = '12 * x ^ 3 + 99 * x ^ 2 + 23 * x + 40 = 0'
poly2 = '12 * x ^ 3 + 18 * x ^ 2 + 23 * x + 37 = 0'
firstpoly.write(poly1)
secondpoly.write(poly2)
firstpoly.close()
secondpoly.close()

#----------------------------------------------------------

first = open('First.txt', 'r')
second = open('Second.txt', 'r')
stringone = first.readline()
stringtwo = second.readline()

resmass = []
polynomial = ''

def splitter(str):
    str = str.replace(' ', '')
    mass = str.split('+')
    return mass

def createnum(mass):
    massfin = []
    for i in range(0, len(mass)):
        linex = ''
        line = mass[i]
        for i in range(0, len(line)):
            if line[i].isdecimal():
                linex += line[i]            
            else: break
        massfin.append(linex)
    return massfin

def notequal(mass1, mass2):
    diff = (len(mass1) - len(mass2))
    for i in range (0, len(mass1)):
        if diff > 0:            
            resmass.append(int(mass1[i]))
        else:
            resmass.append(int(mass1[i]) + int(mass2[-diff]))
        diff -= 1    
    return resmass

massone = splitter(stringone)
masstwo = splitter(stringtwo)
massonefin = createnum(massone)
masstwofin = createnum(masstwo)

if len(massonefin) == len(masstwofin):
    for i in range (0, len(massonefin)):
        resmass.append(int(massonefin[i]) + int(masstwofin[i]))        
elif len(massonefin) > len(masstwofin):
    resmass = notequal(massonefin, masstwofin)
elif len(massonefin) < len(masstwofin):
    resmass = notequal(masstwofin, massonefin)

for i in range (len(resmass)-1, -1, -1):
    if i > 1:
        polynomial += str(resmass[-(i + 1)]) + ' * x ^ ' + str(i) + ' + '
    elif i == 1:
        polynomial += str(resmass[-(i + 1)]) + ' * x + '
    elif i == 0:
        polynomial += str(resmass[-(i + 1)]) + ' = 0'

endpoly = open('Polynom.txt', 'w')
endpoly.write(polynomial)
print(massonefin)
print(masstwofin)
print(polynomial)
endpoly.close()