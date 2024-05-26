class Solution:
  def findMinCost(self, x, y, costX, costY):
    """
    Finds the minimum cost to make two strings identical by deleting characters.

    Args:
      x: The first string.
      y: The second string.
      costX: The cost of deleting a character from x.
      costY: The cost of deleting a character from y.

    Returns:
      The minimum cost to make the strings identical.
    """

    m = len(x)
    n = len(y)

    # Create a DP table to store minimum costs
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Base cases: minimum cost to make empty strings identical
    for i in range(m + 1):
      dp[i][0] = i * costX  # Cost of deleting all characters from x

    for j in range(n + 1):
      dp[0][j] = j * costY  # Cost of deleting all characters from y

    # Fill the DP table
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if x[i - 1] == y[j - 1]:
          # No deletion cost if characters match
          dp[i][j] = dp[i - 1][j - 1]
        else:
          # Minimum cost is the lower of deleting from x or y
          dp[i][j] = min(dp[i - 1][j] + costX, dp[i][j - 1] + costY)

    return dp[m][n]
