from pieces.piece import Piece


class Knight(Piece):
    PIECE_TYPE = "N"
    VALUE = 320

    def __init__(self, x, y, color):
        super().__init__(x, y, color, Knight.PIECE_TYPE, Knight.VALUE)

    def get_possible_moves(self, board):
        return self.get_possible_horizontal_moves(board)

    def clone(self):
        return Knight(self.x, self.y, self.color)
