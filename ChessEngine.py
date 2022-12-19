import numpy as np
from Pieces import Pieces
from Board import Board
row, col = (8, 8)
x_coordinate = 0
y_coordinate = 0
matrix = [[0 for i in range(row)]for j in range(col)]
# bp = Pieces('b', 'p', matrix, x_coordinate, y_coordinate)
# wp = Pieces('w', 'p', matrix, x_coordinate, y_coordinate)
# bk = Pieces('b', 'k', matrix, x_coordinate, y_coordinate)
# wk = Pieces('w', 'k', matrix, x_coordinate, y_coordinate)
# br = Pieces('b', 'r', matrix, x_coordinate, y_coordinate)
# wr = Pieces('w', 'r', matrix, x_coordinate, y_coordinate)
# bb = Pieces('b', 'b', matrix, x_coordinate, y_coordinate)
# wb = Pieces('w', 'b', matrix, x_coordinate, y_coordinate)
# bq = Pieces('b', 'q', matrix, x_coordinate, y_coordinate)
# wq = Pieces('w', 'q', matrix, x_coordinate, y_coordinate)
# bkn = Pieces('b', 'kn', matrix, x_coordinate, y_coordinate)
# wkn = Pieces('w', 'kn', matrix, x_coordinate, y_coordinate)
# black_pieces = [br, bkn, bb, bq, bk, bp]
# white_pieces = [wr, wkn, wb, wq, wk, wp]


class ChessEngine:
    def __init__(self):
        pass


board_obj = Board(matrix)
matrix = board_obj.set_up_black_pieces()
board_obj.set_up_white_pieces()

print(np.matrix(matrix))
# for i in range(8):
#     for j in range(8):
#         print(matrix[i][j].which_piece)
print(matrix[0][7].x_coordinate)
print(matrix[0][7].y_coordinate)
matrix = board_obj.movement(3, 0, 0, 0)
print(matrix[3][0].x_coordinate)
# print(rook+''+rook)
