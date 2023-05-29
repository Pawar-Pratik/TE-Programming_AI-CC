def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

        # Check if there is a queen in the upper-left diagonal
        if board[i] - i == col - row:
            return False

        # Check if there is a queen in the upper-right diagonal
        if board[i] + i == col + row:
            return False

    return True


def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        # Found a solution, add it to the list
        solutions.append(list(board))
        return

    for col in range(n):
        if is_safe(board, row, col):
            # Place the queen at (row, col)
            board[row] = col

            # Recursive call for the next row
            solve_n_queens_util(board, row + 1, n, solutions)

            # Backtrack: Remove the queen from (row, col)
            board[row] = -1


def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


# Get user input for the number of queens
n = int(input("Enter the number of queens: "))

# Solve the n-queens problem
solutions = solve_n_queens(n)

# Print the solutions
print(f"Number of solutions for {n}-queens: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in range(n):
        line = ["Q" if col == solution[row] else "." for col in range(n)]
        print(" ".join(line))
    print()
