import numpy as np
from Pieces import Pieces

#testing

class Board:
    def __init__(self, matrix):
        self.matrix = matrix

    def set_up_black_pieces(self):
        for i in range(8):
            which_piece = 'r'  # input("Which piece:")
            self.matrix[0][i] = Pieces('b', which_piece, self.matrix, 0, i)
        for i in range(8):
            self.matrix[1][i] = Pieces('b', 'p', self.matrix, 1, i)

        return self.matrix

    def set_up_white_pieces(self):
        for i in range(8):
            which_piece = 'r'  # input("Which piece:")
            self.matrix[7][i] = Pieces('w', which_piece, self.matrix, 7, i)
        for i in range(8):
            self.matrix[6][i] = Pieces('w', 'p', self.matrix, 6, i)

        return self.matrix

    # def set_up_white_pieces(self, self.matrix, white_pieces):
    #     for i in range(8):
    #         self.matrix[6][i] = white_pieces[len(white_pieces)-1]
    #     for i in range(8):
    #         if (i <= 4):
    #             self.matrix[7][i] = white_pieces[i]
    #         else:
    #             self.matrix[7][i] = white_pieces[-(i-1)]
    #     return self.self.matrix

    def movement(self, toRow, toColumn, fromRow, fromColoumn):
        piece = self.matrix[fromRow][fromColoumn]
        print(type(piece))
        which_piece = piece.which_piece
        if (which_piece == 'r'):
            if (toRow == fromRow or toColumn == fromColoumn):
                self.matrix[toRow][toColumn] = piece
        return self.matrix
    # to : coordinates [][]
    # from : coordinates [][] yuh
