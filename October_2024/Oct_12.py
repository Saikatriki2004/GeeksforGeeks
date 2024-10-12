class Solution:
    def pairWithMaxSum(self, arr):
        # If the array has fewer than 2 elements, return -1
        if len(arr) < 2:
            return -1
        
        # Initialize the maximum sum to a very small value
        max_sum = float('-inf')
        
        # Traverse the array and find the maximum sum of adjacent pairs
        for i in range(len(arr) - 1):
            current_sum = arr[i] + arr[i + 1]
            max_sum = max(max_sum, current_sum)
        
        return max_sum
