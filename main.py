from go_board import board_size, create_board, display_board
from go_rules import is_valid_move, is_surrounded, capture_stones

board = create_board(board_size)
players = ['X', 'O']
current_player = 0

while True:
    display_board(board)
    player = players[current_player]
    move = input("Player " + player + " move (e.g. 'a1'): ")
    col = ord(move[0]) - ord('a')
    row = int(move[1:]) - 1
    if is_valid_move(board, row, col, player) and not is_surrounded(board, row, col):
        board[row][col] = player
        captured = capture_stones(board, row, col, player)
        if len(captured) > 0:
            print("Player " + player + " captured " + str(len(captured)) + " stones.")
        current_player = (current_player + 1) % 2
    else:
        print("Invalid move.")
