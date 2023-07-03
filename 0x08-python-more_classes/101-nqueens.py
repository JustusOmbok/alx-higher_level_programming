#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """checks if queen cann be placed on the board
    """
    n = len(board)

    for i in range(col):
        if board[row][i] == 1:
            return False


    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1


    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False

        i += 1
        j -= 1

    return True


def solve_n_queens_util(board, col, solutions):
    n = len(board)

    if col == n:

        solution = [[r, c] for r in range(n) for c in range(n) if board[r][c] == 1]
        solutions.append(solution)
        return

    for row in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens_util(board, col + 1, solutions)
            board[row][col] = 0


def solve_n_queens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)


    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, solutions)

    for solution in solutions:
        print(solution)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        solve_n_queens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
