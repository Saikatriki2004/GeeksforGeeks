from typing import List

class Solution:
    def maxTip(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
        # Create a list of orders with the corresponding tips and differences
        orders = [(arr[i], brr[i], abs(arr[i] - brr[i])) for i in range(n)]
        
        # Sort orders based on the absolute difference in descending order
        orders.sort(key=lambda x: x[2], reverse=True)
        
        total_tips = 0
        a_count = 0
        b_count = 0
        
        for a_tip, b_tip, _ in orders:
            if (a_tip >= b_tip and a_count < x) or b_count == y:
                total_tips += a_tip
                a_count += 1
            else:
                total_tips += b_tip
                b_count += 1
                
        return total_tips

# Example usage:
solution = Solution()

n = 5
x = 3
y = 3
arr = [1, 2, 3, 4, 5]
brr = [5, 4, 3, 2, 1]
print(solution.maxTip(n, x, y, arr, brr))  # Output: 21

n = 8
x = 4
y = 4
arr = [1, 4, 3, 2, 7, 5, 9, 6]
brr = [1, 2, 3, 6, 5, 4, 9, 8]
print(solution.maxTip(n, x, y, arr, brr))  # Output: 43

n = 7
x = 3
y = 4
arr = [8, 7, 15, 19, 16, 16, 18]
brr = [1, 7, 15, 11, 12, 31, 9]
print(solution.maxTip(n, x, y, arr, brr))  # Output: 110
