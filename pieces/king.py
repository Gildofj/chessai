from ai.move import Move
from pieces.piece import Piece
from pieces.rook import Rook


class King(Piece):
    PIECE_TYPE = "K"
    VALUE = 20000

    def __init__(self, x, y, color):
        super().__init__(x, y, color, King.PIECE_TYPE, King.VALUE)

    def get_possible_moves(self, board):
        moves = []
        moves.append(self.get_move(board, self.x + 1, self.y))
        moves.append(self.get_move(board, self.x + 1, self.y + 1))
        moves.append(self.get_move(board, self.x, self.y + 1))
        moves.append(self.get_move(board, self.x - 1, self.y + 1))
        moves.append(self.get_move(board, self.x - 1, self.y))
        moves.append(self.get_move(board, self.x - 1, self.y - 1))
        moves.append(self.get_move(board, self.x, self.y - 1))
        moves.append(self.get_move(board, self.x + 1, self.y - 1))
        moves.append(self.get_top_castling_move(board))
        moves.append(self.get_bottom_castling_move(board))

        return self.remove_null_from_list(moves)

    def get_top_castling_move(self, board):
        if (self.color == Piece.WHITE and board.white_king_moved) or (
            self.color == Piece.BLACK and board.black_king_moved
        ):
            return 0

        piece = board.get_piece(self.x, self.y - 3)

        if (
            piece != 0
            and piece.color == self.color
            and piece.piece_type == Rook.PIECE_TYPE
            and board.get_piece(self.x, self.y - 1) == 0
            and board.get_piece(self.x, self.y - 2) == 0
        ):
            return Move(self.x, self.y, self.x, self.y - 2, True)

        return 0

    def get_bottom_castling_move(self, board):
        if (self.color == Piece.WHITE and board.white_king_moved) or (
            self.color == Piece.BLACK and board.black_king_moved
        ):
            return 0

        piece = board.get_piece(self.x, self.y + 4)

        if (
            piece != 0
            and piece.color == self.color
            and piece.piece_type == Rook.PIECE_TYPE
            and board.get_piece(self.x, self.y + 1) == 0
            and board.get_piece(self.x, self.y + 2) == 0
            and board.get_piece(self.x, self.y + 3) == 0
        ):
            return Move(self.x, self.y, self.x, self.y - 2, True)

        return 0

    def clone(self):
        return King(self.x, self.y, self.color)
