from go_board import board, display_board
from go_rules import is_valid_move, is_surrounded

players = ['X', 'O']
current_player = 0

while True:
    display_board(board)
    player = players[current_player]
    move = input("Player " + player + " move (e.g. 'a1'): ")
    col = ord(move[0]) - ord('a')
    row = int(move[1:]) - 1
    if is_valid_move(board, row, col, player):
        board[row][col] = player
        current_player = (current_player + 1) % 2
    else:
        print("Invalid move.")
