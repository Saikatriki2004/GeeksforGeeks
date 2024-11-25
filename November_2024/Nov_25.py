class Solution:
    def maxProduct(self, arr):
        # Initialize variables
        max_so_far = arr[0]
        min_so_far = arr[0]
        result = arr[0]
        
        # Iterate through the array from the second element
        for num in arr[1:]:
            if num < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            
            # Update max and min products
            max_so_far = max(num, max_so_far * num)
            min_so_far = min(num, min_so_far * num)
            
            # Update the result
            result = max(result, max_so_far)
        
        return result
