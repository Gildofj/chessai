from ai.move import Move


class Piece:
    WHITE = "W"
    BLACK = "B"

    def __init__(self, x, y, color, piece_type, value):
        self.x = x
        self.y = y
        self.color = color
        self.piece_type = piece_type
        self.value = value

    def get_possible_diagonal_moves(self, board):
        moves = []
        for i in range(1, 8):
            if not board.in_bounds(self.x + i, self.y + i):
                break
            piece = board.get_piece(self.x + i, self.y + i)
            moves.append(self.get_move(board, self.x + i, self.y + i))
            if piece != 0:
                break

        for i in range(1, 8):
            if not board.in_bounds(self.x + i, self.y - i):
                break
            piece = board.get_piece(self.x + i, self.y - i)
            moves.append(self.get_move(board, self.x + i, self.y - i))
            if piece != 0:
                break

        for i in range(1, 8):
            if not board.in_bounds(self.x - i, self.y - i):
                break
            piece = board.get_piece(self.x - i, self.y - i)
            moves.append(self.get_move(board, self.x - i, self.y - i))
            if piece != 0:
                break

        for i in range(1, 8):
            if not board.in_bounds(self.x - i, self.y + i):
                break
            piece = board.get_piece(self.x - i, self.y + i)
            moves.append(self.get_move(board, self.x - i, self.y + i))
            if piece != 0:
                break

        return self.remove_null_from_list(moves)

    def get_possible_horizontal_moves(self, board):
        moves = []

        # Moves to the right of the piece.
        for i in range(1, 8 - self.x):
            piece = board.get_piece(self.x + i, self.y)
            moves.append(self.get_move(board, self.x + i, self.y))

            if piece != 0:
                break

        # Moves to the left of the piece.
        for i in range(1, self.x + 1):
            piece = board.get_piece(self.x - i, self.y)
            moves.append(self.get_move(board, self.x - i, self.y))
            if piece != 0:
                break

        # Downward moves.
        for i in range(1, 8 - self.y):
            piece = board.get_piece(self.x, self.y + i)
            moves.append(self.get_move(board, self.x, self.y + i))
            if piece != 0:
                break

        # Upward moves.
        for i in range(1, self.y + 1):
            piece = board.get_piece(self.x, self.y - i)
            moves.append(self.get_move(board, self.x, self.y - i))
            if piece != 0:
                break

        return self.remove_null_from_list(moves)

    def get_move(self, board, xto, yto):
        move = 0
        if board.in_bounds(xto, yto):
            piece = board.get_piece(xto, yto)
            if piece != 0:
                if piece.color != self.color:
                    move = Move(self.x, self.y, xto, yto, False)
            else:
                move = Move(self.x, self.y, xto, yto, False)

        return move

    def remove_null_from_list(self, l):
        return [move for move in l if move != 0]

    def to_string(self):
        return self.color + self.piece_type + " "
