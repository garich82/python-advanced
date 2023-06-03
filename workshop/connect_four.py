from collections import deque
from colorama import Fore

def place_circle():
    row = ROWS - 1

    while row >= 0 and board[row][player_col] != "0":
        row -= 1

    board[row][player_col] = player_symbol

    return row


def check_for_win(row, col):
    for x, y in directions:
        count = 1

        for i in range(1, 4):
            new_row = row + x * i
            new_col = col + y * i

            if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
                break

            if board[new_row][new_col] != player_symbol:
                break

            count += 1

        for i in range(1, 4):
            new_row = row - x * i
            new_col = col - y * i

            if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
                break

            if board[new_row][new_col] != player_symbol:
                break

            count += 1

        if count >= 4:
            return True

    return False


def check_for_draw():
    for i in range(COLS):

        if board[0][i] == "0":
            return False

    return True


ROWS, COLS = 6, 7

board = [['0'] * COLS for row in range(ROWS)]

player_one_symbol = Fore.YELLOW + '1' + Fore.RESET
player_two_symbol = Fore.BLUE + '2' + Fore.RESET

turn = deque([['1', player_one_symbol], ['2', player_two_symbol]])

win = False

directions = ((-1, -1), (1, -1), (1, 0), (0, -1))

while not win:
    [print(f"[{', '.join(row)}]") for row in board]

    player_number, player_symbol = turn[0]

    try:
        player_col = int(input(f"Player {player_number}, please choose a column: ")) - 1
    except ValueError:
        print(Fore.RED + f"Select a valid number from 1 to {COLS}" + Fore.RESET)
        continue

    if not 0 <= player_col < COLS:
        print(Fore.RED + f"Select a valid number from 1 to {COLS}" + Fore.RESET)
        continue

    if board[0][player_col] != "0":
        print(Fore.RED + "This column is full, please select another column!" + Fore.RESET)
        continue

    row = place_circle()
    win = check_for_win(row, player_col)

    if check_for_draw():
        break

    turn.rotate()

if win:
    print(f"Player {turn[-1][0]} wins!")
else:
    print(f"Game ends in a draw!")

[print(f"[{', '.join(row)}]") for row in board]
