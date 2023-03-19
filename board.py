board_size = 9
board = [[' ' for _ in range(board_size)] for _ in range(board_size)]


def display_board(board):
    print(' ', end=' ')
    for i in range(board_size):
        print(chr(ord('a')+i), end=' ')
    print()
    for i in range(board_size):
        print(i+1, end=' ')
        for j in range(board_size):
            print(board[i][j], end=' ')
        print()
