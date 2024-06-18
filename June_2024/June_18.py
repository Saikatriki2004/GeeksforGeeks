class Solution:
    def rectanglesInCircle(self, r):
        count = 0
        for a in range(1, 2 * r + 1):
            for b in range(1, 2 * r + 1):
                if a * a + b * b <= 4 * r * r:
                    count += 1
        return count

# Example usage
sol = Solution()
print(sol.rectanglesInCircle(1))  # Output: 1
print(sol.rectanglesInCircle(2))  # Output: 8
