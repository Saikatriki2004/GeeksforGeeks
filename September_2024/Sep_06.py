class Solution:
    ##Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        # Initialize the variables
        max_so_far = arr[0]  # To store the maximum sum found so far
        max_ending_here = arr[0]  # To store the current subarray sum
        
        # Iterate through the array starting from the second element
        for i in range(1, len(arr)):
            # Update max_ending_here to include current element or start new subarray
            max_ending_here = max(arr[i], max_ending_here + arr[i])
            
            # Update max_so_far if max_ending_here is larger
            max_so_far = max(max_so_far, max_ending_here)
        
        # Return the maximum sum found
        return max_so_far
if __name__ == "__main__":
    sol = Solution()
    
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    result = sol.maxSubArraySum(arr)
    print(f"Maximum contiguous subarray sum is {result}")  # Output should be 7
