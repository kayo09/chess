import numpy as np
from Pieces import Pieces
from Board import Board
row, col = (8, 8)
matrix = [[0 for i in range(row)]for j in range(col)]
bp = Pieces('b', 'p', matrix)
wp = Pieces('w', 'p', matrix)
bk = Pieces('b', 'k', matrix)
wk = Pieces('w', 'k', matrix)
br = Pieces('b', 'r', matrix)
wr = Pieces('w', 'r', matrix)
bb = Pieces('b', 'b', matrix)
wb = Pieces('w', 'b', matrix)
bq = Pieces('b', 'q', matrix)
wq = Pieces('w', 'q', matrix)
bkn = Pieces('b', 'kn', matrix)
wkn = Pieces('w', 'kn', matrix)
black_pieces = [br, bkn, bb, bq, bk, bp]
white_pieces = [wr, wkn, wb, wq, wk, wp]


class ChessEngine:
    def __init__(self):
        pass


board_obj = Board(matrix)
matrix = board_obj.set_up_black_pieces(matrix, black_pieces)
print(board_obj.get_index(wr))
print(np.matrix(matrix))
