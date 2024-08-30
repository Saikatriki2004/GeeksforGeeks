class Solution:
    def nQueen(self, n):
        def solve_nq_util(board, row, solutions):
            # If all queens are placed
            if row == n:
                solution = []
                for i in range(n):
                    for j in range(n):
                        if board[i][j] == 1:
                            solution.append(j + 1)
                solutions.append(solution)
                return

            # Try placing the queen in all columns one by one
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 1
                    solve_nq_util(board, row + 1, solutions)
                    board[row][col] = 0

        def is_safe(board, row, col):
            # Check this column on upper side
            for i in range(row):
                if board[i][col] == 1:
                    return False

            # Check upper diagonal on left side
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False

            # Check upper diagonal on right side
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == 1:
                    return False

            return True

        solutions = []
        board = [[0 for _ in range(n)] for _ in range(n)]
        solve_nq_util(board, 0, solutions)
        return solutions

# Example usage
solution = Solution()
n = 9
result = solution.nQueen(n)
for sol in result:
    print(sol)
