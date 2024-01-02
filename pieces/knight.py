from pieces.piece import Piece


class Knight(Piece):
    PIECE_TYPE = "N"
    VALUE = 320

    def __init__(self, x, y, color):
        super().__init__(x, y, color, Knight.PIECE_TYPE, Knight.VALUE)

    def get_possible_moves(self, board):
        moves = []

        moves.append(self.get_move(board, self.x + 2, self.y + 1))
        moves.append(self.get_move(board, self.x - 1, self.y + 2))
        moves.append(self.get_move(board, self.x - 2, self.y + 1))
        moves.append(self.get_move(board, self.x + 1, self.y - 2))
        moves.append(self.get_move(board, self.x + 2, self.y - 1))
        moves.append(self.get_move(board, self.x + 1, self.y + 2))
        moves.append(self.get_move(board, self.x - 2, self.y - 1))
        moves.append(self.get_move(board, self.x - 1, self.y - 2))

        return self.remove_null_from_list(moves)

    def clone(self):
        return Knight(self.x, self.y, self.color)
