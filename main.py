from typing import List, Tuple, Union

EMPTY = 0
BLACK = 1
WHITE = 2

class GoBoard:
    def __init__(self, size: int):
        self.size = size
        self.board = [[EMPTY for _ in range(size)] for _ in range(size)]
        self.current_player = BLACK
        self.previous_board = None

    def place_stone(self, row: int, col: int) -> bool:
        if self.board[row][col] != EMPTY:
            return False

        self.previous_board = [row[:] for row in self.board]
        self.board[row][col] = self.current_player
        
        captured_stones = self._capture_stones(row, col)
        if captured_stones:
            for stone in captured_stones:
                self.board[stone[0]][stone[1]] = EMPTY
        
        if self._is_suicide(row, col):
            self.board = self.previous_board
            return False
        
        self.current_player = BLACK if self.current_player == WHITE else WHITE
        return True

    def _capture_stones(self, row: int, col: int) -> List[Tuple[int, int]]:
        captured_stones = []
        
        for r, c in self._get_adjacent_intersections(row, col):
            if self.board[r][c] != EMPTY and self._is_surrounded(r, c):
                captured_stones.append((r, c))
        
        return captured_stones
    
    def _is_surrounded(self, row: int, col: int) -> bool:
        return all(self.board[r][c] != EMPTY for r, c in self._get_adjacent_intersections(row, col))
    
    def _get_adjacent_intersections(self, row: int, col: int) -> List[Tuple[int, int]]:
        intersections = []
        
        if row > 0:
            intersections.append((row-1, col))
        if row < self.size-1:
            intersections.append((row+1, col))
        if col > 0:
            intersections.append((row, col-1))
        if col < self.size-1:
            intersections.append((row, col+1))
        
        return intersections

    def _is_suicide(self, row: int, col: int) -> bool:
        if not self._is_surrounded(row, col):
            return False
        
        for r, c in self._get_adjacent_intersections(row, col):
            if self.board[r][c] != self.current_player:
                return False
        
        return True

    def get_board(self) -> List[List[int]]:
        return self.board


def display_board(board: List[List[int]]):
    size = len(board)
    
    print("   ", end="")
    for i in range(size):
        print(chr(i+ord('a')), end=" ")
    print()
    
    print("  +" + "--" * size + "-+")
    
    for i in range(size):
        print(f"{size-i:2d}|", end=" ")
        for j in range(size):
            stone = board[i][j]
            if stone == BLACK:
                print(u"● ", end="")
            elif stone == WHITE:
                print(u"○ ", end="")
            else:
                print("+ ", end="")
        print(f"|{size-i:2d}")
    
    print("  +" + "--" * size + "-+")
    print("   ", end="")
    for i in range(size):
        print(chr(i+ord('a')), end=" ")
    print()


def main():
    size = 9
    board = GoBoard(size)
    
    while True:
        display_board(board.get_board())
        player = "Black" if board.current_player == BLACK else "White"
        print(f"{player}'s turn")
        
        move = get_move(size)
        if move == "resign":
            print(f"{player} resigns")
            break
        elif move == "pass":
            print(f"{player} passes")
            board.current_player = BLACK if board.current_player == WHITE else WHITE
        else:
            row, col = move
            success = board.place_stone(row, col)
            if not success:
                print("Invalid move")
            else:
                print(f"{player} places a stone at ({chr(col+ord('a'))}, {size-row})")
    
    display_board(board.get_board())


def get_move(size: int) -> Union[str, Tuple[int, int]]:
    while True:
        move_str = input("Enter your move (e.g. 'a1' or 'pass' or 'resign'): ")
        if move_str == "pass" or move_str == "resign":
            return move_str
        
        if len(move_str) != 2:
            print("Invalid move")
            continue
        
        col_str, row_str = move_str
        if not col_str.isalpha() or not row_str.isdigit():
            print("Invalid move")
            continue
        
        col = ord(col_str.lower()) - ord('a')
        row = size - int(row_str)
        if row < 0 or row >= size or col < 0 or col >= size:
            print("Invalid move")
            continue
        
        return (row, col)


if __name__ == "__main__":
    main()

