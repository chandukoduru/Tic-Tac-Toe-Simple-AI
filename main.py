"""
Tic-Tac-Toe with Simple AI
The human player is X and the computer is O.
The computer uses the Minimax algorithm to choose its moves.
"""

HUMAN = "X"
COMPUTER = "O"
EMPTY = " "


def display_board(board):
    """Display the current 3x3 board."""
    print()
    for row in range(3):
        print(" " + " | ".join(board[row * 3:(row + 1) * 3]))
        if row < 2:
            print("---+---+---")
    print()


def get_winner(board):
    """Return X or O if a player has won; otherwise return None."""
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    for a, b, c in winning_lines:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]

    return None


def is_draw(board):
    """A draw occurs when every cell is filled and nobody has won."""
    return get_winner(board) is None and EMPTY not in board


def minimax(board, is_maximizing):
    """
    Evaluate possible future moves.
    +1 means the computer wins, -1 means the human wins, 0 means draw.
    """
    winner = get_winner(board)

    if winner == COMPUTER:
        return 1
    if winner == HUMAN:
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for index in range(9):
            if board[index] == EMPTY:
                board[index] = COMPUTER
                score = minimax(board, False)
                board[index] = EMPTY
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for index in range(9):
            if board[index] == EMPTY:
                board[index] = HUMAN
                score = minimax(board, True)
                board[index] = EMPTY
                best_score = min(best_score, score)
        return best_score


def computer_move(board):
    """Choose the best available move using Minimax."""
    best_score = -float("inf")
    best_move = None

    for index in range(9):
        if board[index] == EMPTY:
            board[index] = COMPUTER
            score = minimax(board, False)
            board[index] = EMPTY

            if score > best_score:
                best_score = score
                best_move = index

    return best_move


def human_move(board):
    """Read and validate the human player's move (positions 1 to 9)."""
    while True:
        choice = input("Choose a position (1-9): ").strip()

        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Please enter a number from 1 to 9.")
            continue

        index = int(choice) - 1
        if board[index] != EMPTY:
            print("That position is already occupied. Choose another.")
            continue

        return index


def main():
    """Play one complete game."""
    board = [str(number) for number in range(1, 10)]

    # Empty cells are represented by their position until selected.
    print("TIC-TAC-TOE WITH SIMPLE AI")
    print("You are X. The computer is O.")
    print("Select positions using the numbers shown below.")

    display_board(board)

    # Convert the numbered starting board into empty cells for game logic.
    board = [EMPTY] * 9

    while True:
        move = human_move(board)
        board[move] = HUMAN
        display_board(board)

        if get_winner(board) == HUMAN:
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        print("Computer is thinking...")
        move = computer_move(board)
        board[move] = COMPUTER
        display_board(board)

        if get_winner(board) == COMPUTER:
            print("Computer wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()
