from typing import List

class Solution:
    def zigZag(self, n: int, arr: List[int]) -> None:
        # Traverse all array elements
        for i in range(n - 1):
            # If the current index is even
            if i % 2 == 0:
                # If the current element is greater than the next element
                if arr[i] > arr[i + 1]:
                    # Swap the elements
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            # If the current index is odd
            else:
                # If the current element is less than the next element
                if arr[i] < arr[i + 1]:
                    # Swap the elements
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Example usage:
solution = Solution()

n = 7
arr = [4, 3, 7, 8, 6, 2, 1]
solution.zigZag(n, arr)
print(arr)  # Output: [3, 7, 4, 8, 2, 6, 1]

n = 4
arr = [1, 4, 3, 2]
solution.zigZag(n, arr)
print(arr)  # Output: [1, 4, 2, 3]
