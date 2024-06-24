class Solution:
    def sumMatrix(self, n, q):
        start = max(1, q - n)
        end = min(n, q - 1)
        if start > end:
            return 0
        return end - start + 1

# Example usage:
sol = Solution()
print(sol.sumMatrix(4, 7))  # Output: 2
print(sol.sumMatrix(5, 4))  # Output: 3
