class Board:
    WIDTH = 8
    HEIGHT = 8

    def __init__(self, chesspieces, white_king_moves, black_king_moves):
        self.chesspieces = chesspieces
        self.white_king_moves = white_king_moves
        self.black_king_moves = black_king_moves

    @classmethod
    def clone(cls):
        chess_pieces = [[o for x in range(Board.WIDTH) for y in range(Board.HEIGHT)]]
