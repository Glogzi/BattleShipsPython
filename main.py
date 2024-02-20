import bs


if __name__ == '__main__':
    print("set board size:")
    size = bs.set_board_size()
    print("set amount of ships")
    ships_num = bs.set_ships_num(size)
    print("player 1 now will set ships")
    b1 = bs.set_ships(ships_num, size)
    b12 = bs.create_board(size)
    print("that's your board, do not show it to player 2")
    bs.enter_to_clear()
    print("to let player 2 set ships click enter")
    bs.enter_to_clear()
    print("player 2 now will set ships")
    b2 = bs.set_ships(ships_num, size)
    b22 = bs.create_board(size)
    print("that's your board, do not show it to player 1")
    print("click enter to continue")
    bs.enter_to_clear()
    winner = ""
    while True:
        bs.next_round("player1", b1, b2, b12)
        if bs.check_win(b2, ships_num):
            winner = "player1"
            break
        bs.next_round("player2", b2, b1, b22)
        if bs.check_win(b1, ships_num):
            winner = "player2"
            break
    print(f"player {winner} won!")
    input()
