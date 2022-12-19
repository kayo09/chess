import numpy as np
from Pieces import Pieces
from Board import Board


checkmate = False

row, col = (8, 8)
matrix = [["-" for i in range(row)]for j in range(col)]
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


def castle(color): # this will make the king and rook swap positions if they are in initial position
    if (color == white_pieces):
        if (matrix[0][0] == "r" and matrix[0][4] == "k"):
            print ("white rook and king are in initial position, we can castle")
            matrix[0][0], matrix[0][4] = matrix[0][4], matrix[0][0]
            
    elif(color == black_pieces):
        if (matrix[7][0] == br and matrix[0][4] == wk):
            print("rook and king are in initial position, we can castle")
            matrix[7][0], matrix[0][4] = matrix[0][4], matrix[7][0]
            
def promote(color): # If a pawn reaches the other end, it becomes a king
    if (color == white_pieces):
        for x in range (7):
            if (matrix[7][x == wp]):
                x = wq
    
    if (color == black_pieces):
        for x in range (7):
            if (matrix[0][x == wp]):
                x = bq            
    
def hello(color): 
    print("POOP")
    
# class Play:
    
    
    
#     if (checkmate == False):
#             print("hewo")
            
            
#     # try:
#     #     newlist.append(dlist[1])
#     # except IndexError:
#     #     print("move is out of bounds") 
    
#     Play
            
        
    
    
