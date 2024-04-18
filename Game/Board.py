from string import ascii_uppercase

HORIZONTAL_SYMBOL = ascii_uppercase[:10]
VERTICAL_SYMBOL = list(range(1, 11))
COLS = 10
ROWS = 10
BOARD_FILLER = "~"


class Board:
    def __init__(self):
        self.game_board = self.generate_empty_board()

    def generate_empty_board(self):
        return [[BOARD_FILLER] * COLS for _ in range(10)]

    def display_board(self):
        for num in VERTICAL_SYMBOL:
            print(' ', num, end='')
        print()
        itr = 0
        for i in self.game_board:
            print(HORIZONTAL_SYMBOL[itr], end=' ')
            print('  '.join(i))
            itr += 1

board = Board()
board.display_board()