import random

# global variable
MAIN_ARRAY = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def PrintGrid():
    print(*MAIN_ARRAY[0:3])
    print(*MAIN_ARRAY[3:6])
    print(*MAIN_ARRAY[6:9])


def IsCellEmpty(arr, pos):
    return arr[pos - 1] == '-'


def Move(who, pos):
    if who == 'X': PLayerMove(pos)
    if who == 'O': BotMoveSmart()
    # if who == 'O': BotMoveRand()


def PLayerMove(pos):
    MAIN_ARRAY[pos - 1] = 'X'


def IsWin(arr, char):
    # row and column
    for i in range(3):
        if (arr[i * 3 + 0] == arr[i * 3 + 1] == arr[i * 3 + 2] == char) or (
                arr[i + 0] == arr[i + 3] == arr[i + 6] == char):
            return True
    # diagonals
    if (arr[0] == arr[4] == arr[8] == char) or (arr[2] == arr[4] == arr[6] == char):
        return True

    # otherwise
    return False


def GetRandValidCell(samples):
    print(samples)
    eci = []
    for i in range(len(samples)):
        if MAIN_ARRAY[samples[i]-1] == '-': eci.append(samples[i])

    if len(eci) > 0:
        print(eci)
        return random.choice(eci)
    else:
        return False


def BotMoveRand():
    eci = []
    for i in range(9):
        if MAIN_ARRAY[i] == '-': eci.append(i)

    pos_index = random.choice(eci)
    MAIN_ARRAY[pos_index] = 'O'


def CheckForWin(char):
    # print('test 0')
    for i in range(9):
        temp_arr = MAIN_ARRAY.copy()
        # print('test 1')
        if IsCellEmpty(temp_arr, i + 1):
            # print('test 2')
            temp_arr[i] = char
            if IsWin(temp_arr, char):
                # print('test 3')
                return i + 1

    return False

def TryMove(pos):
    if pos:
        MAIN_ARRAY[pos - 1] = 'O'
        return True

def PlayerAt(poses):
    for i in poses:
        if MAIN_ARRAY[i - 1] == 'X': return True
    return False

def TryMoveChain(arrays):
    for a in arrays:
        if TryMove(GetRandValidCell(a)): return

    # any other choice is error
    print('Error at TryMoveChain func')



def BotMoveSmart():
    # check for bot's immediate win -> win
    if TryMove(CheckForWin('O')): return

    # check for player's immediate win -> block him
    if TryMove(CheckForWin('X')): return

    # ===============================================

    # player's first choice is at corner
    if PlayerAt([1, 3, 7, 9]):
        TryMoveChain([
            [5],
            [2, 4, 6, 8],
            [1, 3, 7, 9]
        ]); return


    # player's first choice is at side
    if PlayerAt([2, 4, 6, 8]):
        # there is still an option (with two x's on 2-6 for example) to lose,
        # but I'm to lazy to check every option or bruteforce it
        TryMoveChain([
            [5],
            [1, 3, 7, 9],
            [2, 4, 6, 8]
        ]); return

    # player's first choice is at center
    if PlayerAt([5]):
        TryMoveChain([
            [1, 3, 7, 9],
            [2, 4, 6, 8]
        ]); return

    # any other choice is error
    print('Error at ifs')


def InputIsNotLegit(pos):
    return pos < 1 or pos > 9 or not IsCellEmpty(MAIN_ARRAY, pos)


def GetPlayerPosition():
    try:
        return int(input("Where wanna place 'X'?\n"))
    except:
        return -1


def IsDraw():
    if '-' not in MAIN_ARRAY:
        print("It is a DRAW, ggwp bro")
        PrintGrid()
        return True

    return False


# start game loop
while True:
    # pos is int type
    player_pos = GetPlayerPosition()

    # check if input is valid, otherwise back to prompt
    if InputIsNotLegit(player_pos): continue

    Move('X', player_pos)
    if IsWin(MAIN_ARRAY, 'X'):
        print("You WIN")
        PrintGrid()
        break

    if IsDraw(): break

    Move('O', player_pos)
    if IsWin(MAIN_ARRAY, 'O'):
        print("You LOSE")
        PrintGrid()
        break

    PrintGrid()
