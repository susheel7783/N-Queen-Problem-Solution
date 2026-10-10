# N-Queens using backtracking
# Place N queens on an N x N board so that no two queens attack each other.
# A queen attacks along its row, its column, and both diagonals.

N = 8  # board size (and number of queens)

# board[row] = column of the queen in that row, or -1 if the row is empty.
# One queen per row is built in, so row conflicts never happen.
board = [-1] * N


def safe(row, col):
    """True if a queen at (row, col) is not attacked by queens in rows 0..row-1."""
    for r in range(row):      # check every earlier row
        c = board[r]              # column of the queen in row r

        # Same column: vertical attack
        if c == col:
            return False

        # Same diagonal: row distance equals column distance
        if abs(c - col) == abs(r - row):
            return False

    return True               # no conflicts found


def solve(row):
    """Fill rows row..N-1. Return True once a full valid arrangement is found."""

    # Base case: every row has a queen, so the puzzle is solved
    if row == N:
        return True

    for col in range(N):         # try each column in this row
        if safe(row, col):         # is this square safe?
            board[row] = col          # place the queen (choose)

            if solve(row + 1):      # fill the remaining rows (explore)
                return True

            board[row] = -1           # dead end: remove the queen (backtrack)

    return False                  # no column worked, caller must move its queen


def print_board():
    """Print the board: Q = queen, . = empty square."""
    for row in range(N):
        line = ""
        for col in range(N):
            line += "Q " if board[row] == col else ". "
        print(line)


if __name__ == "__main__":
    if solve(0):                 # start from the first row
        print(f"Solved! {N} queens, 0 attacks\n")
        print_board()
        print("\nColumn per row:", board)
    else:
        print("No solution exists for N =", N)