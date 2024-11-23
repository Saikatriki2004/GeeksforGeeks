class Solution:
    def getMinDiff(self, k, arr):
        n = len(arr)
        
        # If there is only one tower, no need to modify, the difference is always 0
        if n == 1:
            return 0
        
        # Sort the array to simplify the process of finding the min and max
        arr.sort()
        
        # Initialize the result as the initial difference between the max and min heights
        initial_diff = arr[-1] - arr[0]
        
        # Initialize minimum possible difference
        min_diff = initial_diff
        
        # The first tower (smallest) and the last tower (largest)
        # Try modifying each tower by increasing or decreasing by k
        for i in range(1, n):
            # Get the minimum height by decreasing the largest tower and increasing the smallest tower
            smallest = min(arr[0] + k, arr[i] - k)
            largest = max(arr[-1] - k, arr[i - 1] + k)
            
            # The difference after the modifications
            min_diff = min(min_diff, largest - smallest)
        
        return min_diff
