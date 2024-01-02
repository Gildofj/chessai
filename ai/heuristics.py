import numpy

from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.piece import Piece
from pieces.queen import Queen
from pieces.rook import Rook


class Heuristics:
    PAWN_TABLE = numpy.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [5, 10, 10, -20, -20, 10, 10, 5],
            [5, -5, -10, 0, 0, -10, -5, 5],
            [0, 0, 0, 20, 20, 0, 0, 0],
            [5, 5, 10, 25, 25, 10, 5, 5],
            [10, 10, 20, 30, 30, 20, 10, 10],
            [50, 50, 50, 50, 50, 50, 50, 50],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )

    KNIGHT_TABLE = numpy.array(
        [
            [-50, -40, -30, -30, -30, -30, -40, -50],
            [-40, -20, 0, 5, 5, 0, -20, -40],
            [-30, 5, 10, 15, 15, 10, 5, -30],
            [-30, 0, 15, 20, 20, 15, 0, -30],
            [-30, 5, 15, 20, 20, 15, 0, -30],
            [-30, 0, 10, 15, 15, 10, 0, -30],
            [-40, -20, 0, 0, 0, 0, -20, -40],
            [-50, -40, -30, -30, -30, -30, -40, -50],
        ]
    )

    BISHOP_TABLE = numpy.array(
        [
            [-20, -10, -10, -10, -10, -10, -10, -20],
            [-10, 5, 0, 0, 0, 0, 5, -10],
            [-10, 10, 10, 10, 10, 10, 10, -10],
            [-10, 0, 10, 10, 10, 10, 0, -10],
            [-10, 5, 5, 10, 10, 5, 5, -10],
            [-10, 0, 5, 10, 10, 5, 0, -10],
            [-10, 0, 0, 0, 0, 0, 0, -10],
            [-20, -10, -10, -10, -10, -10, -10, -20],
        ]
    )

    ROOK_TABLE = numpy.array(
        [
            [0, 0, 0, 5, 5, 0, 0, 0],
            [-5, 0, 0, 0, 0, 0, 0, -5],
            [-5, 0, 0, 0, 0, 0, 0, -5],
            [-5, 0, 0, 0, 0, 0, 0, -5],
            [-5, 0, 0, 0, 0, 0, 0, -5],
            [-5, 0, 0, 0, 0, 0, 0, -5],
            [5, 10, 10, 10, 10, 10, 10, 5],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )

    QUEEN_TABLE = numpy.array(
        [
            [-20, -10, -10, -5, -5, -10, -10, -20],
            [-10, 0, 5, 0, 0, 0, 0, -10],
            [-10, 5, 5, 5, 5, 5, 0, -10],
            [0, 0, 5, 5, 5, 5, 0, -5],
            [-5, 0, 5, 5, 5, 5, 0, -5],
            [-10, 0, 5, 5, 5, 5, 0, -10],
            [-10, 0, 0, 0, 0, 0, 0, -10],
            [-20, -10, -10, -5, -5, -10, -10, -20],
        ]
    )

    @staticmethod
    def evaluate(board):
        material = Heuristics.get_material_score(board)

        pawns = Heuristics.get_piece_position_score(
            board, Pawn.PIECE_TYPE, Heuristics.PAWN_TABLE
        )
        knights = Heuristics.get_piece_position_score(
            board, Knight.PIECE_TYPE, Heuristics.KNIGHT_TABLE
        )
        bishops = Heuristics.get_piece_position_score(
            board, Bishop.PIECE_TYPE, Heuristics.BISHOP_TABLE
        )
        rooks = Heuristics.get_piece_position_score(
            board, Rook.PIECE_TYPE, Heuristics.ROOK_TABLE
        )
        queens = Heuristics.get_piece_position_score(
            board, Queen.PIECE_TYPE, Heuristics.QUEEN_TABLE
        )

        return material + pawns + knights + bishops + rooks + queens

    @staticmethod
    def get_piece_position_score(board, piece_type, table):
        white = 0
        black = 0
        for x in range(8):
            for y in range(8):
                piece = board.chesspieces[x][y]
                if piece != 0:
                    if piece.piece_type == piece_type:
                        if piece.color == Piece.WHITE:
                            white += table[x][y]
                        else:
                            black += table[7 - x][y]

        return white - black

    @staticmethod
    def get_material_score(board):
        white = 0
        black = 0
        for x in range(8):
            for y in range(8):
                piece = board.chesspieces[x][y]
                if piece != 0:
                    if piece.color == Piece.WHITE:
                        white += piece.value
                    else:
                        black += piece.value

        return white - black
