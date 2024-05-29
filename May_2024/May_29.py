class Solution:
    def findWinner(self, n: int, x: int, y: int) -> int:
        # Create a dp array of size n + 1, initialized to False
        dp = [False] * (n + 1)
        
        # Base cases
        dp[0] = False  # If no coins left, player to move loses
        dp[1] = True   # If 1 coin left, Geek can pick it and win
        
        # Fill the dp array using the relation defined above
        for i in range(2, n + 1):
            # If picking 1 coin leads to a losing state for opponent
            if i - 1 >= 0 and not dp[i - 1]:
                dp[i] = True
            # If picking x coins leads to a losing state for opponent
            elif i - x >= 0 and not dp[i - x]:
                dp[i] = True
            # If picking y coins leads to a losing state for opponent
            elif i - y >= 0 and not dp[i - y]:
                dp[i] = True
            else:
                dp[i] = False
        
        # The result for n coins is in dp[n]
        return 1 if dp[n] else 0

# Example usage:
solution = Solution()
print(solution.findWinner(5, 3, 4))  # Output: 1
print(solution.findWinner(2, 3, 4))  # Output: 0
