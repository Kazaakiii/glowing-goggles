def display(board):
    print("\n  1 2 3")
    for row_number, row in enumerate(board, 1):
        print(f"{row_number} " + "|".join(row))
        if row_number < 3:
            print("  -+-+-")


def has_won(board, mark):
    lines = board + [list(column) for column in zip(*board)]
    lines += [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]
    return any(all(cell == mark for cell in line) for line in lines)


def get_move(board, player):
    while True:
        move = input(f"Player {player}, enter row and column (example: 2 3): ").split()
        if len(move) != 2 or not all(part.isdigit() for part in move):
            print("Enter two numbers from 1 to 3.")
            continue
        row, column = int(move[0]) - 1, int(move[1]) - 1
        if not (0 <= row < 3 and 0 <= column < 3):
            print("Both numbers must be from 1 to 3.")
        elif board[row][column] != " ":
            print("That square is already taken.")
        else:
            return row, column


def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    for turn in range(9):
        player = "X" if turn % 2 == 0 else "O"
        display(board)
        row, column = get_move(board, player)
        board[row][column] = player
        if has_won(board, player):
            display(board)
            print(f"Player {player} wins!")
            return
    display(board)
    print("It is a draw.")


if __name__ == "__main__":
    play()
