from go_board import board_size

def is_valid_move(board, row, col, player):
    if board[row][col] != ' ':
        return False
    board[row][col] = player
    if is_surrounded(board, row, col):
        board[row][col] = ' '
        return False
    board[row][col] = ' '
    return True

def is_surrounded(board, row, col):
    if row > 0 and board[row-1][col] == ' ':
        return False
    if row < board_size-1 and board[row+1][col] == ' ':
        return False
    if col > 0 and board[row][col-1] == ' ':
        return False
    if col < board_size-1 and board[row][col+1] == ' ':
        return False
    return True
