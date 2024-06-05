class Solution:
    def findSwapValues(self, a, n, b, m):
        sumA = sum(a)
        sumB = sum(b)

        # The difference must be even to be able to swap and balance the sums
        if (sumA - sumB) % 2 != 0:
            return -1

        # The value we need to find a corresponding pair
        target = (sumA - sumB) // 2

        # Convert one of the lists to a set for O(1) average time complexity lookups
        setB = set(b)

        for val in a:
            # Find the value in setB that would balance the arrays if swapped
            if val - target in setB:
                return 1

        return -1

# Example usage:
solution = Solution()

n = 6
m = 4
a = [4, 1, 2, 1, 1, 2]
b = [3, 6, 3, 3]
print(solution.findSwapValues(a, n, b, m))  # Output: 1

n = 4
m = 4
a = [5, 7, 4, 6]
b = [1, 2, 3, 8]
print(solution.findSwapValues(a, n, b, m))  # Output: 1
