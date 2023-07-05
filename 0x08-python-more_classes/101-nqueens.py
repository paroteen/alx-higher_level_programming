import sys

def is_safe(board, row, col):
    # Check if a queen can be placed at board[row][col]
    # without conflicting with any other queens

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_nqueens(board, col):
    # Base case: All queens have been placed
    if col >= N:
        print_solution(board)
        return True

    # Try placing a queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1)
            board[i][col] = 0

def print_solution(board):
    # Print the current board configuration
    solution = []
    for i in range(N):
        row = []
        for j in range(N):
            if board[i][j] == 1:
                row.append([i, j])
        solution.append(row)
    print(solution)

if __name__ == "__main__":
    # Read the command-line argument
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N-Queens problem
    solve_nqueens(board, 0)
