import numpy as np
from Pieces import Pieces

# testing


class Board:
    def __init__(self, matrix):
        self.matrix = matrix

    def set_up_black_pieces(self):
        for i in range(8):
            which_piece = input("Which piece:")
            self.matrix[0][i] = Pieces('b', which_piece, self.matrix, 0, i)
        for i in range(8):
            self.matrix[1][i] = Pieces('b', 'p', self.matrix, 1, i)

        return self.matrix

    def set_up_white_pieces(self):
        for i in range(8):
            which_piece = input("Which piece:")
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
        which_piece = piece.which_piece
        if (which_piece == 'r'):
            if (toRow == fromRow or toColumn == fromColoumn):
                if (self.can_move(piece)):
                    self.matrix[fromRow][fromColoumn] = 0
                    self.matrix[toRow][toColumn] = piece
        if (which_piece == 'kn'):
            if ((toRow == fromRow+2 and toColumn == fromColoumn+1) or (toRow == fromRow+1 and toColumn == fromColoumn+2)):
                if (self.can_move(piece)):
                    self.matrix[fromRow][fromColoumn] = 0
                    self.matrix[toRow][toColumn] = piece
        if (which_piece == 'b'):
            dx = abs(toRow-fromRow)
            dy = abs(toColumn-fromColoumn)
            if (dx == dy) and (dx > 0):
                if (self.can_move(piece)):
                    self.matrix[fromRow][fromColoumn] = 0
                    self.matrix[toRow][toColumn] = piece
        if (which_piece == 'q'):
            if (self.can_move(piece)):
                self.matrix[fromRow][fromColoumn] = 0
                self.matrix[toRow][toColumn] = piece

        self.print_board
        return self.matrix

    def can_move(self, fromRow, fromColoumn, toRow, toColoumn, piece):
        capture = []
        move = True
        while (toRow != fromRow) or (toColoumn != fromColoumn):
            x = fromRow+1
            y = fromColoumn+1
            if (self.matrix[x][y] != 0):
                if (self.matrix[x][y].team == piece.team):
                    print(
                        f"illegal move since a team piece is present at the location{x}{y}")
                    move = False
                else:
                    capture.append(self.matrix[x][y])
                    move = True
            else:
                move = True

            self.can_move(x, y, toRow, toColoumn, piece)
        return move

    def print_board(self):
        for i in range(0, 8*8):
            row = i//8
            col = i % 8
            if (self.matrix[row][col] != 0):
                print(self.matrix[row][col].which_piece, end=' ')
            else:
                print(self.matrix[row][col], end=' ')

    def castle(self, piece):  # this will make the king and rook swap positions if they are in initial position
        if (piece.team == 'w'):
            if (self.matrix[0][0] == "r" and self.matrix[0][4] == "k"):
                print("white rook and king are in initial position, we can castle")
                self.matrix[0][0], self.matrix[0][4] = self.matrix[0][4], self.matrix[0][0]

        elif (piece.team == 'b'):
            if (self.matrix[7][0] == 'r' and self.matrix[0][4] == 'k'):
                print("rook and king are in initial position, we can castle")
                self.matrix[7][0], self.matrix[0][4] = self.matrix[0][4], self.matrix[7][0]

    def promote(self, piece):  # If a pawn reaches the other end, it becomes a king
        if (piece.team == 'w'):
            for x in range(7):
                if (self.matrix[7][x == 'p']):
                    x = input("which piece should the pawn be promoted to: ")

        if (piece.team == 'b'):
            for x in range(7):
                if (self.matrix[0][x == 'p']):
                    x = input("which piece should the pawn be promoted to: ")
                    
                    
    def pieceValue(piece):
        
        obj = Pieces
        
        if obj.which_piece == 'p':
            return 1
        elif obj.which_piece == 'kn': 
            return 3
        elif obj.which_piece == 'b':
            return 3
        elif obj.which_piece == 'r':
            return 5
        elif obj.which_piece == 'q':
            return 6
        elif obj.which_piece == 'k':
            return 100
        
    def calcScore(matrix):
        totalScore = 0
        for i in range(7):
            for j in range(7):
                totalScore = totalScore + Board.pieceValue[i,j]
                
    