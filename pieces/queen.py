from pieces.piece import Piece


class Queen(Piece):
    PIECE_TYPE = "Q"
    VALUE = 900

    def __init__(self, x, y, color):
        super().__init__(x, y, color, Queen.PIECE_TYPE, Queen.VALUE)

    def get_possible_moves(self, board):
        horizontal = self.get_possible_horizontal_moves(board)
        diagonal = self.get_possible_diagonal_moves(board)
        return horizontal + diagonal

    def clone(self):
        return Queen(self.x, self.y, self.color)
