from simple_chalk import chalk

print("")
titleColor = chalk.bgRed.white.bold
print(titleColor("Chess AI || CLI Game"))
print("")


def get_user_move():
    print("")
    print(chalk.bgGreen.bold.black("Example Move: A1 A2"))
    move_str = input(chalk.bgBlue.white.underline("Your Move >>>"))
    move_str = move_str.replace(" ", "")


def get_valid_user_move(board):
    while True:
        pass


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

while True:
    pass
