class Solution:
    def swapNibbles(self, n: int) -> int:
        # Swap the nibbles
        return ((n & 0x0F) << 4) | (n >> 4)

# Example usage:
solution = Solution()
print(solution.swapNibbles(100))  # Output: 70
print(solution.swapNibbles(129))  # Output: 24
