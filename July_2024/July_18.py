from typing import List

class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # Initialize lengths of longest alternating subsequences
        up = 1
        down = 1
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up = down + 1
            elif arr[i] < arr[i - 1]:
                down = up + 1
        
        # The maximum length of alternating subsequence
        return max(up, down)

# Example usage
sol = Solution()
arr1 = [1, 5, 4]
print(sol.alternatingMaxLength(arr1))  # Output: 3

arr2 = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
print(sol.alternatingMaxLength(arr2))  # Output: 7
