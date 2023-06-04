from collections import deque

SIZE = 3
board = [[str(i), str(i+1), str(i+2)] for i in range(1, SIZE * SIZE + 1, SIZE)]
players = deque()


def print_board(begin=False):
    if begin:
        print("This is numeration of the board:")
        [print(f"| {' | '.join(row)} |") for row in board]


def start():
    player_one_name = input("Player 1, please enter your name: ")
    player_two_name = input("Player 2, please enter your name: ")

    while True:
        player_one_symbol = input(f"{player_one_name}, would you like to play with ✖ or ○: ").upper()

        if player_one_symbol not in ["X", "O"]:
            print(f"{player_one_symbol} is not a valid symbol, please type letter X or letter O!")
        else:
            break

    player_two_symbol = "○" if player_one_symbol == "X" else "✖"
    player_one_symbol = "✖" if player_two_symbol == "○" else "○"

    print(f"{player_one_name} will play with {player_one_symbol}")
    print(f"{player_two_name} will play with {player_two_symbol}")
    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])

    print_board(begin=True)


start()



