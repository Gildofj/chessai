from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.piece import Piece
from pieces.queen import Queen
from pieces.rook import Rook


class Board:
    WIDTH = 8
    HEIGHT = 8

    def __init__(self, chesspieces, white_king_moved, black_king_moved):
        self.chesspieces = chesspieces
        self.white_king_moved = white_king_moved
        self.black_king_moved = black_king_moved

    @classmethod
    def clone(cls):
        chess_pieces = [[o for x in range(Board.WIDTH) for y in range(Board.HEIGHT)]]

        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                piece = chessboard.chesspieces[x][y]
                if piece != 0:
                    chesspieces[x][y] = piece.clone()

        return cls(
            chesspieces, chessboard.white_king_moved, chessboard.black_king_moved
        )

    @classmethod
    def new(cls):
        chess_pieces = [[0 for x in range(Board.WIDTH)] for y in range(Board.HEIGHT)]

        # Creating Pawns
        for x in range(Board.WIDTH):
            chess_pieces[x][Board.HEIGHT - 2] = Pawn(x, Board.HEIGHT - 2, Piece.WHITE)
            chess_pieces[x][1] = Pawn(x, 1, Piece.BLACK)

        # Creating Rooks
        chess_pieces[0][Board.HEIGHT - 1] = Rook(0, Board.HEIGHT - 1, Piece.WHITE)
        chess_pieces[0][0] = Rook(0, 0, Piece.BLACK)
        chess_pieces[Board.WIDTH - 1][0] = Rook(Board.WIDTH - 1, 0, Piece.BLACK)

        # Creating Knights
        chess_pieces[1][Board.HEIGHT - 1] = Knight(1, Board.HEIGHT - 1, Piece.WHITE)
        chess_pieces[Board.WIDTH - 2][Board.HEIGHT - 1] = Knight(
            Board.WIDTH - 2, Board.HEIGHT - 1, Piece.WHITE
        )
        chess_pieces[1][0] = Knight(1, 0, Piece.BLACK)
        chess_pieces[Board.WIDTH - 2][0] = Knight(Board.WIDTH - 2, 0, Piece.BLACK)

        # Creating Bishops
        chess_pieces[2][Board.HEIGHT - 1] = Bishop(2, Board.HEIGHT - 1, Piece.WHITE)
        chess_pieces[Board.WIDTH - 3][Board.WIDTH - 1] = Bishop(
            Board.HEIGHT - 3, Board.WIDTH - 1, Piece.WHITE
        )
        chess_pieces[2][0] = Bishop(2, 0, Piece.BLACK)
        chess_pieces[Board.HEIGHT - 3][0] = Bishop(Board.HEIGHT - 3, 0, Piece.BLACK)

        # Creating the King and the Queen
        chess_pieces[4][Board.HEIGHT - 1] = King(4, Board.HEIGHT - 1, Piece.WHITE)
        chess_pieces[3][Board.HEIGHT - 1] = Queen(3, Board.HEIGHT - 1, Piece.WHITE)
        chess_pieces[4][0] = King(4, 0, Piece.BLACK)
        chess_pieces[3][0] = Queen(3, 0, Piece.BLACK)

        return cls(chess_pieces, False, False)

    def get_possible_moves(self, color):
        moves = []
        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                piece = self.chesspieces[x][y]
                if piece != 0 and piece.color == color:
                    moves += piece.get_possible_moves(self)

        return moves

    def perform_move(self, move):
        piece = self.chesspieces[move.xfrom][move.yfrom]
        piece.x = move.xto
        piece.y = move.yto
        self.chesspieces[move.xto][move.yto] = piece
        self.chesspieces[move.xfrom][move.yfrom] = 0

        if piece.piece_type == Pawn.PIECE_TYPE and (
            piece.y == 0 or piece.y == Board.HEIGHT - 1
        ):
            self.chesspieces[piece.x][piece.y] = Queen(piece.x, piece.y, piece.color)

        if move.castling_move:
            if move.xto < move.xfrom:
                rook = self.chesspieces[move.xfrom][0]
                rook.x = 2
                self.chesspieces[2][0] = rook
                self.chesspieces[0][0] = 0
            if move.xto > move.xfrom:
                rook = self.chesspieces[move.xfrom][Board.HEIGHT - 1]
                rook.x = Board.WIDTH - 4
                self.chesspieces[Board.WIDTH - 4][Board.HEIGHT - 1] = rook
                self.chesspieces[move.xfrom][Board.HEIGHT - 1] = 0

        if piece.piece_type == King.PIECE_TYPE:
            if piece.color == Piece.WHITE:
                self.white_king_moved = True
            else:
                self.black_king_moved = True

    def is_check(self, color):
        other_color = Piece.WHITE
        if color == Piece.WHITE:
            other_color = Piece.BLACK

        for move in self.get_possible_moves(other_color):
            copy = Board.clone(self)
            copy.perform_move(move)

            king_found = False

            for x in range(Board.WIDTH):
                for y in range(Board.HEIGHT):
                    piece = copy.chesspieces[x][y]
                    if (
                        piece != 0
                        and piece.color == color
                        and piece.piece_type == King.PIECE_TYPE
                    ):
                        king_found = True

            if not king_found:
                return True

            return False
