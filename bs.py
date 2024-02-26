import numpy as np
import os


def set_ships_num(br_size):
    inp = 2
    while True:
        noterr = True
        try:
            inp = int(input(">"))
        except:
            noterr = False
        if inp > (br_size**2) - 1:
            noterr = False
        if inp < 1:
            noterr = False
        if not noterr:
            print("incorrect number of ships, number cannot be larger or as large as board, and smaller than 1")
            continue
        break
    return inp


def set_board_size():
    inp = 5
    while True:
        noterr = True
        try:
            inp = int(input(">"))
        except:
            noterr = False
        if inp > 9:
            noterr = False
        if inp < 2:
            noterr = False
        if not noterr:
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
    print("example: \"b 3\" (remember about space). this will place ship on b3 tile")
    alpha = list("|abcdefghi")
    while True:
        board = create_board(br_size)
        print_board(board)
        error = False
        err_message = ""
        for i in range(ships):
            player_input = input(">")
            player_input = player_input.lower()
            input_array = player_input.split(" ")
            try:
                y = alpha.index(input_array[0])
                print(y)
            except ValueError:
                err_message = "y coords error"
                error = True
                break
            if "0" in input_array or "|" in input_array:
                err_message = "invalid tile error"
                error = True
                break
            else:
                try:
                    if board[y, int(input_array[1])] == "|":
                        err_message = "occupied error"
                        error = True
                        break
                    else:
                        board[y, int(input_array[1])] = "|"
                except IndexError:
                    err_message = "x coords error"
                    error = True
                    break
            print_board(board)
        if not error:
            return board
        print("error, set ships again, now correctly")
        print(err_message)


def create_board(br_size):
    board = np.zeros((br_size+1, br_size+1), dtype=str)
    board[:,] = "#"
    alpha = list("|abcdefghi")
    for i in range(len(board)):
        board[0, i] = str(i)
    for i in range(len(board)):
        board[i, 0] = alpha[i]
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


def next_round(player, board, enemy_board):
    print(f"{player} round, click enter to continue")
    enter_to_clear()
    print("that's your board")
    print_board(board)
    print("where you wanna shoot? (write x and y  cords like when setting ships)")
    alpha = list("|abcdefghi")
    while True:
        error = False
        player_input = input(">")
        input_array = player_input.split(" ")
        y = alpha.index(input_array[0])
        if "0" in input_array:
            error = True
        else:
            try:
                if enemy_board[y, int(input_array[1])] == "|":
                    print("hit and sink (tell it to the 2nd player)")
                    enemy_board[y, int(input_array[1])] = "X"
            except:
                error = True
        if not error:
            return board
        print("error, set tiles again, now correctly")
