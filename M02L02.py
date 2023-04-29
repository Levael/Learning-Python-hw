import random

array = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def PrintGrid(grid):
    print(*grid[0:3])
    print(*grid[3:6])
    print(*grid[6:9])


def IsCellEmpty(arr, pos):
    return arr[pos-1] == '-'


def Move(who, pos, arr):
    if who == 'X': PLayerMove(arr, pos)
    if who == 'O': BotMoveRand(arr)

def PLayerMove(arr, pos):
    arr[pos-1] = 'X'


def IsWin(arr, char):
    # row and column
    for i in range(3):
        if (arr[i*3+0] == arr[i*3+1] == arr[i*3+2] == char) or (arr[i+0] == arr[i+3] == arr[i+6] == char):
            return True
    # diagonals
    if (arr[0] == arr[4] == arr[8] == char) or (arr[2] == arr[4] == arr[6] == char):
        return True

    # otherwise
    return False


def BotMoveRand(arr):
    eci = []
    for i in range(9):
        if arr[i] == '-': eci.append(i)

    pos_index = random.choice(eci)
    arr[pos_index] = 'O'


def IsAllOk(arr, pos):
    return pos < 1 or pos > 9 or not IsCellEmpty(arr, pos)


def GetPlayerPosition():
    return int(input("Where wanna place 'X'?\n"))


def IsDraw(arr):
    if '-' not in arr:
        print("It is a DRAW, ggwp bro")
        PrintGrid(arr)
        return True

    return False


# start game loop
while True:
    # pos is int type
    player_pos = GetPlayerPosition()

    # check if input is valid, otherwise back to prompt
    if IsAllOk(array, player_pos): continue

    Move('X', player_pos, array)
    if IsWin(array, 'X'):
        print("You WIN")
        PrintGrid(array)
        break

    if IsDraw(array): break

    Move('O', player_pos, array)
    if IsWin(array, 'O'):
        print("You LOSE")
        PrintGrid(array)
        break

    PrintGrid(array)