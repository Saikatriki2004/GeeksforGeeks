class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        # Initialize variables
        max_sum = float('-inf')  # Stores the maximum sum found
        current_sum = 0  # Stores the current subarray sum
        
        for num in arr:
            # Update the current sum (either start fresh or continue the subarray)
            current_sum = max(num, current_sum + num)
            # Update the maximum sum if the current sum is larger
            max_sum = max(max_sum, current_sum)
        
        return max_sum
