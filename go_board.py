board_size = 9

def create_board(size):
    board = [[' ' for x in range(size)] for y in range(size)]
    return board

def display_board(board):
    print("  ", end="")
    for i in range(board_size):
        print(chr(i + ord('a')), end=" ")
    print()
    for i in range(board_size):
        print("{:2d}".format(i+1), end=" ")
        for j in range(board_size):
            print(board[i][j], end=" ")
        print()