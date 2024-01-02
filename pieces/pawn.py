from pieces.piece import Piece


class Pawn(Piece):
    PIECE_TYPE = "P"
    VALUE = 100

    def __init__(self, x, y, color):
        super().__init__(x, y, color, Pawn.PIECE_TYPE, Pawn.VALUE)

    def is_starting_position(self):
        if self.color == Piece.BLACK:
            return self.y == 1

        return self.y == 8 - 2

    def get_possible_moves(self, board):
        moves = []

        # Direction the pawm can move in.
        direction = -1
        if self.color == Piece.BLACK:
            direction = 1

        # The general 1 step forward move.
        if board.get_piece(self.x, self.y + direction) == 0:
            moves.append(self.get_move(board, self.x, self.y + direction))

        # The Pawn can take 2 steps as the first move.
        if (
            self.is_starting_position()
            and board.get_piece(self.x, self.y + direction) == 0
            and board.get_piece(self.x, self.y + direction * 2) == 0
        ):
            moves.append(self.get_move(board, self.x, self.y + direction * 2))

        # Eating pieces.
        piece = board.get_piece(self.x + 1, self.y + direction)
        if piece != 0:
            moves.append(self.get_move(board, self.x + 1, self.y + direction))

        piece = board.get_piece(self.x - 1, self.y + direction)
        if piece != 0:
            moves.append(self.get_move(board, self.x - 1, self.y + direction))

        return self.remove_null_from_list(moves)

    def clone(self):
        return Pawn(self.x, self.y, self.color)
