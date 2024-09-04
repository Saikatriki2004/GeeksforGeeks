class Solution:
    def nthStair(self, n):
        # The number of unique ways to reach the nth stair
        # can be calculated as n//2 + 1
        return (n // 2) + 1

# Example usage
sol = Solution()
n = 4
print(sol.nthStair(n))  # Output should be 3
