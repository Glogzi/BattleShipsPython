import numpy as np
import os


def enter_to_clear():
    input(">")
    os.system("cls || clear")


def print_board(board):
    for line in board:
        for column in line:
            print(column, end="")
        print("")


def set_ships(board, ships, size):
    print("set ship by writing coordinates where you want to place it")
    print("example: \"2 3\". this will place ship on x=2 y=3 tile")
    while True:
        error = False
        for i in range(ships):
            player_input = input(">")
            input_array = player_input.split(" ")
            if "0" in input_array:
                error = True
            else:
                try:
                    if board[int(input_array[1]), int(input_array[0])] == "|":
                        error = True
                    else:
                        board[int(input_array[1]), int(input_array[0])] = "|"
                except:
                    error = True
        if not error:
            return board
        board = create_board(size)
        print("error, set tiles again, now correctly")


def create_board(size):
    board = np.zeros((size+1, size+1), dtype=str)
    board[:,] = "#"
    for i in range(len(board)):
        board[0, i] = str(i)
    for i in range(len(board)):
        board[i, 0] = str(i)
    board[0, 0] = " "
    return board


def next_round(player, board, enemy_board):
    print(f"{player} round, click enter to continue")
    enter_to_clear()
    print("that's your board")
    print_board(board)
    print("where you wanna shoot? (write x and y  cords like when setting ships)")
    while True:
        error = False
        is_ship = False
        player_input = input(">")
        input_array = player_input.split(" ")
        if "0" in input_array:
            error = True
        else:
            try:
                if board[int(input_array[1]), int(input_array[0])] == "|":
                    is_ship = True
                    print("hit and sink (tell it to the 2nd player)")
                    enemy_board[int(input_array[1]), int(input_array[0])] = "X"
            except:
                error = True
        if not error:
            return board
        print("error, set tiles again, now correctly")


if __name__ == '__main__':
    b1 = create_board(5)
    b2 = create_board(5)

    print("player 1 now will set ships")
    set_ships(b1, 2, 5)
    print("that's your board, do not show it to player 2")
    print_board(b1)
    print("to let player 2 set ships click enter")
    enter_to_clear()
    print("player 2 now will set ships")
    set_ships(b2, 2, 5)
    print("that's your board, do not show it to player 1")
    print_board(b2)
    print("click enter to continue")
    enter_to_clear()
    next_round("player1", b1, b2)
    next_round("player2", b2, b1)


