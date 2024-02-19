import numpy as np
import os


def set_ships_num(br_size):
    inp = 2
    while True:
        not_err = True
        try:
            inp = int(input(">"))
        except ValueError:
            not_err = False
        if inp > br_size:
            not_err = False
        if inp < 1:
            not_err = False
        if not not_err:
            print("incorrect number of ships, number cannot be larger or equal to board size, and smaller than 1")
            continue
        break
    return inp


def set_board_size():
    inp = 5
    while True:
        not_err = True
        try:
            inp = int(input(">"))
        except ValueError:
            not_err = False
        if inp > 9:
            not_err = False
        if inp < 2:
            not_err = False
        if not not_err:
            print("incorrect board size, please enter size not larger than 9 and not smaller than 2")
            continue
        break
    return inp


def enter_to_clear():
    input(">")
    os.system("cls||clear")


def print_board(board):
    for line in board:
        for column in line:
            print(column, end="")
        print("")


def set_ships(ships, br_size):
    print("set ship by writing coordinates where you want to place it")
    print("example: \"2 3\". this will place ship on x=2 y=3 tile")
    while True:
        board = create_board(br_size)
        print_board(board)
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
                except (IndexError, ValueError):
                    error = True
            print_board(board)
        if not error:
            return board
        print("error, set ships again, now correctly")


def create_board(br_size):
    board = np.zeros((br_size+1, br_size+1), dtype=str)
    board[:,] = "#"
    for i in range(len(board)):
        board[0, i] = str(i)
    for i in range(len(board)):
        board[i, 0] = str(i)
    board[0, 0] = " "
    return board


def check_win(board, ships):
    count = 0
    for arr in board:
        for tile in arr:
            if tile == "X":
                count += 1
    if count == ships:
        return True
    return False


def next_round(player, board, enemy_board, hidden_enemy_board):
    print(f"{player} round, click enter to continue")
    enter_to_clear()
    print("that's your board")
    print_board(board)
    print("that's enemy board")
    print_board(hidden_enemy_board)
    print("where you wanna shoot? (write x and y  cords like when setting ships)")
    while True:
        error = False
        player_input = input(">")
        input_array = player_input.split(" ")
        if "0" in input_array:
            error = True
        else:
            try:
                if enemy_board[int(input_array[1]), int(input_array[0])] == "|":
                    print("hit and sink (tell it to the 2nd player)")
                    enemy_board[int(input_array[1]), int(input_array[0])] = "X"
                    hidden_enemy_board[int(input_array[1]), int(input_array[0])] = "X"
                else:
                    print("miss")
                    hidden_enemy_board[int(input_array[1]), int(input_array[0])] = "-"
            except (IndexError, ValueError):
                error = True
        if not error:
            return board
        print("error, set tiles again, now correctly")
