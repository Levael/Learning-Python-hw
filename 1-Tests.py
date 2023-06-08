import numpy as np

# Создайте пустую доску 3x3 с помощью библиотеки NumPy
board = np.MAIN_ARRAY([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
current_player = "X"  # Игрок, который делает ход первым

def print_board():
    print("  0 1 2")
    for i in range(3):
        row_str = f"{i} "
        for j in range(3):
            row_str += f"{board[i][j]} "
        print(row_str)

def make_move(player):
    print(f"Ход игрока {player}")
    row = int(input("Введите номер строки: "))
    col = int(input("Введите номер столбца: "))

    # Проверка на возможность хода
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        print("Невозможно сделать ход в этой ячейке!")
        return False

def check_win():
    # Проверка по строкам и столбцам
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    # Проверка по диагоналям
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    # Ничья
    if " " not in board:
        print("Ничья!")
        return True

    return False

while True:
    print_board()
    if make_move(current_player):
        if check_win():
            print_board()
            print(f"Игрок {current_player} победил!")
            break
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"