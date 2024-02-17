import numpy as np


def create_board(size):
    board = np.zeros((size+1, size+1), dtype=str)
    board[:,] = "#"
    for i in range(len(board)):
        board[0, i] = str(i)
    for i in range(len(board)):
        board[i, 0] = str(i)
    board[0,0] = " "
    return board


if __name__ == '__main__':
    b1 = create_board(5)
    for i in b1:
        for j in i:
            print(j, end="")
        print("")