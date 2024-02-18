import numpy as np
import os


def enter_to_clear():
    input(">")
    os.system("cls||clear")


def print_board(board):
    for line in board:
        for column in line:
            print(column, end="")
        print("")


def set_ships(ships, size):
    print("set ship by writing coordinates where you want to place it")
    print("example: \"2 3\". this will place ship on x=2 y=3 tile")
    while True:
        board = create_board(size)
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
                except:
                    error = True
            print_board(board)
        if not error:
            return board
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
            except:
                error = True
        if not error:
            return board
        print("error, set tiles again, now correctly")


if __name__ == '__main__':
    print("player 1 now will set ships")
    b1 = set_ships(2, 5)
    print("that's your board, do not show it to player 2")
    print_board(b1)
    print("to let player 2 set ships click enter")
    enter_to_clear()
    print("player 2 now will set ships")
    b2 = set_ships(2, 5)
    print("that's your board, do not show it to player 1")
    print_board(b2)
    print("click enter to continue")
    enter_to_clear()
    winner = ""
    while True:
        next_round("player1", b1, b2)
        if check_win(b2, 2):
            winner = "player1"
            break
        next_round("player2", b2, b1)
        if check_win(b1, 2):
            winner = "player2"
            break
    print(f"player {winner} won!")
    input()
