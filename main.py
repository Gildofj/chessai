import os
import sys

from simple_chalk import chalk

from ai.ai import AI
from ai.move import Move
from board import Board
from pieces.piece import Piece

sys.path.append(os.path.abspath(os.path.join("pieces")))
sys.path.append(os.path.abspath(os.path.join("ai")))


print("")
titleColor = chalk.bgMagenta.black.bold
print(titleColor("Chess AI || CLI Game"))
print("")


def get_user_move():
    print("")
    print(chalk.bgGreen.bold.black("Example Move: A1 A2"))
    move_str = input(chalk.bgMagentaBright.black.underline("Your Move >>> "))
    move_str = move_str.replace(" ", "")

    try:
        xfrom = letter_to_xpos(move_str[0:1])
        yfrom = 8 - int(move_str[1:2])
        xto = letter_to_xpos(move_str[2:3])
        yto = 8 - int(move_str[3:4])
        return Move(xfrom, yfrom, xto, yto, False)
    except ValueError:
        print(chalk.bgWhite.red.bold.underline("Invalid format. Example: A2 A4"))
        return get_user_move()


def get_valid_user_move(board):
    while True:
        move = get_user_move()
        valid = False
        possible_moves = board.get_possible_moves(Piece.WHITE)
        if not possible_moves:
            return 0

        for possible_move in possible_moves:
            if move.equals(possible_move):
                move.castling_move = possible_move.castling_move
                valid = True
                break

        if valid:
            break

        print("Invalid move!")

    return move


def letter_to_xpos(letter):
    letter = letter.upper()
    if letter == "A":
        return 0

    if letter == "B":
        return 1

    if letter == "C":
        return 2

    if letter == "D":
        return 3

    if letter == "E":
        return 4

    if letter == "F":
        return 5

    if letter == "G":
        return 6

    if letter == "H":
        return 7

    raise ValueError("Invalid letter.")


print("Here is the board")

board = Board.new()
print(board.to_string())
while True:
    move = get_valid_user_move(board)
    if move == 0:
        if board.is_check(Piece.WHITE):
            print("Checkmate! Black Wins")
            break
        else:
            print("Stalemate.")
            break

    board.perform_move(move)
    print("User move: " + move.to_string())
    print(board.to_string())

    ai_move = AI.get_ai_move(board, [])
    if ai_move == 0:
        if board.is_check(Piece.BLACK):
            print("Checkmate! White Wins")
            break
        else:
            print("Stalemate.")
            break

    board.perform_move(ai_move)
    print("AI move: " + ai_move.to_string())
    print(board.to_string())
