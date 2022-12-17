import numpy as np
from Pieces import Pieces


class Board:
    def __init__(self, matrix):
        self.matrix = matrix

    def set_up_black_pieces(self, matrix, black_pieces):
        for i in range(8):
            matrix[1][i] = black_pieces[len(black_pieces)-1]
        for i in range(8):
            if (i <= 4):
                matrix[0][i] = black_pieces[i]
            else:
                matrix[0][i] = black_pieces[-(i-1)]
        return self.matrix

    def set_up_white_pieces(self, matrix, white_pieces):
        for i in range(8):
            matrix[6][i] = white_pieces[len(white_pieces)-1]
        for i in range(8):
            if (i <= 4):
                matrix[7][i] = white_pieces[i]
            else:
                matrix[7][i] = white_pieces[-(i-1)]
        return self.matrix
