class Solution:
    def getSingle(self, arr):
        result = 0
        # XOR all elements
        for num in arr:
            result ^= num
        return result

# Example usage:
solution = Solution()
print(solution.getSingle([1, 1, 2, 2, 2]))  # Output: 2
print(solution.getSingle([8, 8, 7, 7, 6, 6, 1]))  # Output: 1
