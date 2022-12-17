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
black_pieces = [br.type, bkn.type, bb.type, bq.type, bk.type, bp.type]
white_pieces = [wr.type, wkn.type, wb.type, wq.type, wk.type, wp.type]


class ChessEngine:
    def __init__(self):
        pass


board_obj = Board(matrix)
matrix = board_obj.set_up_black_pieces(matrix, black_pieces)
board_obj.set_up_white_pieces(matrix, white_pieces)
print(np.matrix(matrix))
rook = matrix[0][0]
# print(rook.type+''+rook.type)
