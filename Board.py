import numpy as np
from Pieces import Pieces


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
        if (which_piece == 'r'):  # for rook
            if (toRow == fromRow or toColumn == fromColoumn):
                self.matrix[toRow][toColumn] = piece
        if (which_piece == 'kn'):
            if ((toRow == fromRow+2 and toColumn == fromColoumn+1) or (toRow == fromRow+1 and toColumn == fromColoumn+2)):
                self.matrix[toRow][toColumn] = piece
        if (which_piece == 'b'):
            pass
        return self.matrix

    def castle(color):  # this will make the king and rook swap positions if they are in initial position
        if (color == white_pieces):
            if (matrix[0][0] == "r" and matrix[0][4] == "k"):
                print("white rook and king are in initial position, we can castle")
                matrix[0][0], matrix[0][4] = matrix[0][4], matrix[0][0]

        elif (color == black_pieces):
            if (matrix[7][0] == br and matrix[0][4] == wk):
                print("rook and king are in initial position, we can castle")
                matrix[7][0], matrix[0][4] = matrix[0][4], matrix[7][0]

    def promote(color):  # If a pawn reaches the other end, it becomes a king
        if (color == white_pieces):
            for x in range(7):
                if (matrix[7][x == wp]):
                    x = wq

    if (color == black_pieces):
        for x in range(7):
            if (matrix[0][x == wp]):
                x = bq
    # to : coordinates [][]
    # from : coordinates [][]
