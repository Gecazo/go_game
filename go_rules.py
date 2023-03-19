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

def capture_stones(board, row, col, player):
    captured = []
    # check for captures in all four directions
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        r, c = row + dr, col + dc
        if r < 0 or r >= board_size or c < 0 or c >= board_size:
            continue
        if board[r][c] == ' ':
            continue
        if board[r][c] == player:
            continue
        if is_surrounded(board, r, c):
            captured.append((r, c))
            # remove captured stones from the board
            board[r][c] = ' '
    return captured
