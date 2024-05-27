from typing import List


class Solution:
  def longestSubseq(self, n: int, a: List[int]) -> int:
    # Initialize a DP table to store the length of the longest subsequence ending at each index
    dp = [1] * n

    # Iterate through the array
    for i in range(1, n):
      # Find the longest subsequence ending at a previous index where the difference is 1
      for j in range(i):
        if abs(a[i] - a[j]) == 1:
          # Update dp[i] if the current subsequence length (1 + dp[j]) is greater
          dp[i] = max(dp[i], 1 + dp[j])

    # Return the maximum length of a subsequence found
    return max(dp)
