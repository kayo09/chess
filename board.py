class Board:
    def __init__(self):
        rows, cols = (8, 8)
        board = [[0]*cols]*rows
        print(board)


obj = Board

# checks for piece potential moves compatibility


def potential_moves_for_pieces(obj):
    where_piece_is(obj)  # returns position


def where_piece_is(obj):
    obj.location


def valid_moves():  # just for board compatibility
    pass  # move has to be within range of the board
    print("hello")
