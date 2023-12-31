from pieces.piece import Piece


class Rook(Piece):
    PIECE_TYPE = "R"
    VAUE = 500

    def __init__(self, x, y, color):
        super().__init__(x, y, color, Rook.PIECE_TYPE, Rook.VAUE)

    def get_possible_moves(self, board):
        return self.get_possible_horizontal_moves(board)

    def clone(self):
        return Rook(self.x, self.y, self.color)
