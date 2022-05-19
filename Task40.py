# 40.	*Создайте программу для игры в "Крестики-нолики".

field = [[], [], []]
players = []
win = False
mark = 'Х'
correct = True

for i in range (0, 3):
    field.append([])
    for j in range (0, 3):
        field[j].append(' ')

def massPrint (field):
    print(field[0])
    print(field[1])
    print(field[2])

def wrongCheck(correct):
    if field[int(move[1]) - 1][int(move[0]) - 1] != ' ':
        print('Неправильный ход!')
        correct = False
        return correct

def winner(win): #Это совершенно упоротая проверка, но другую пока не придумал, а через OR работать отказывается :)
    if (field[0][0] == field[0][1] == field[0][2] !=" "):
        win = True
        return win
    if (field[1][0] == field[1][1] == field[1][2] !=" "):
        win = True
        return win
    if (field[2][0] == field[2][1] == field[2][2] !=" "):
        win = True
        return win
    if (field[0][0] == field[1][0] == field[2][0] !=" "):
        win = True
        return win
    if (field[1][0] == field[1][1] == field[1][2] !=" "):
        win = True
        return win
    if (field[2][0] == field[2][1] == field[2][2] !=" "):
        win = True
        return win
    if (field[0][0] == field[1][1] == field[2][2] !=" "):
        win = True
        return win
    if (field[0][2] == field[1][1] == field[2][0] !=" "):
        win = True
        return win

print('Введите имена игроков.')
players.append(input('Игрок 1:'))
players.append(input('Игрок 2:'))
activePlayer = 0
massPrint(field)

while not win:
    correct = True
    inpMove = input(f'{players[activePlayer]}, Ваш ход: ')    
    move = inpMove.split(',')    
    wrongCheck(correct)  
    
    if correct:
        field[int(move[1]) - 1][int(move[0]) - 1] = mark
        if winner(win): break
        if activePlayer == 0: 
            activePlayer = 1
            mark = '0'
        else: 
            activePlayer = 0
            mark = 'Х'
    massPrint(field)

massPrint(field)
print(f'{players[activePlayer]} победил!')