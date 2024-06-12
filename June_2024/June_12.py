class Solution:
    def countNumberswith4(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            if '4' in str(i):
                count += 1
        return count

# Example usage:
solution = Solution()

n = 9
print(solution.countNumberswith4(n))  # Output: 1

n = 44
print(solution.countNumberswith4(n))  # Output: 9

n = 100
print(solution.countNumberswith4(n))  # Output: 19
