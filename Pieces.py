class Pieces:
    def __init__(self, team, type, matrix):
        self.team = team
        self.type = type
        self.matrix = matrix

    def which_piece(self, piece_obj):
        if piece_obj == 'r':
            self.rook()

    def rook(self, matrix):
        pass
