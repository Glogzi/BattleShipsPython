import numpy as np


def print_board(board):
    for line in board:
        for column in line:
            print(column, end="")
        print("")


def set_ships(board, ships):
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
                    board[int(input_array[1]), int(input_array[0])] = "|"
                except:
                    error = True
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


if __name__ == '__main__':
    b1 = create_board(5)
    b2 = create_board(5)

    set_ships(b1, 2)
    print_board(b1)
