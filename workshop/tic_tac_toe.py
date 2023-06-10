from collections import deque
from pyfiglet import Figlet
import speech_recognition as sr


def get_name(player_number):
    while True:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print(f"{player_number}, please say your name: ")


            audio = r.record(source, duration=3)
            print("Recognizing ...")


            try:
                return r.recognize_google(audio)
            except sr.exceptions.UnknownValueError:
                print("Name not recognized. You will have to say your name again!")

def check_for_win():
    player_name, player_symbol = players[0]

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(SIZE)])
    second_diagonal_win = all([board[i][SIZE - i - 1] == player_symbol for i in range(SIZE)])

    row_win = any([all(player_symbol == pos for pos in row) for row in board])
    col_win = any([all(board[r][c] == player_symbol for r in range(SIZE)) for c in range(SIZE)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print(f"{player_name} won!")

        raise SystemExit

def place_symbol(row, col):
    board[row][col] = players[0][1]

    print_board()
    check_for_win()

    if turns == SIZE * SIZE:
        print("Draw!")
        raise SystemExit


    players.rotate()


def choose_position():
    global turns

    while True:
        try:
            position = int(input(f"{players[0][0]}, choose a free position in the range [1-{SIZE*SIZE}]: "))
            row, col = (position - 1) // SIZE, (position - 1) % SIZE
        except ValueError:
            print(f"{players[0][0]}, please select a valid position!")
            continue

        if 1 <= position <= SIZE * SIZE and board[row][col] == " ":
            turns += 1
            place_symbol(row, col)
        else:
            print(f"{players[0][0]}, please select a valid position between 1 and {SIZE*SIZE}!")


def print_board(begin=False):
    if begin:
        print("This is numeration of the board:")
        [print(f"| {' | '.join(row)} |") for row in board]

        for row in range(SIZE):
            for col in range(SIZE):
                board[row][col] = " "

    else:
        [print(f"| {' | '.join(row)} |") for row in board]


def start():
    figlet = Figlet(font="big")
    print(figlet.renderText("Tic-Tac-Toe"))

    player_one_name = get_name("Player one")
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
    choose_position()


SIZE = 3
turns = 0
board = [[str(i), str(i+1), str(i+2)] for i in range(1, SIZE * SIZE + 1, SIZE)]
players = deque()

start()



