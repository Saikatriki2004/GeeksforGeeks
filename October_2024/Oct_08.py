from typing import List

class Solution:
    def pairsum(self, arr: List[int]) -> int:
        # Initialize two variables to store the two largest values
        first = second = float('-inf')
        
        # Traverse the array to find the largest and second largest numbers
        for num in arr:
            if num > first:
                # Update first and second
                second = first
                first = num
            elif num > second:
                # Update only second if num is smaller than first but larger than second
                second = num
        
        # Return the sum of the two largest numbers
        return first + second

# Example usage:
sol = Solution()
print(sol.pairsum([12, 34, 10, 6, 40]))  # Output: 74
print(sol.pairsum([10, 20, 30]))         # Output: 50
