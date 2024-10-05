class Solution:
    def findSmallest(self, arr):
        # Initialize the smallest positive integer that cannot be represented
        res = 1
        
        # Traverse the sorted array
        for num in arr:
            # If the current number is greater than the smallest unrepresentable sum (res), break
            if num > res:
                break
            
            # Otherwise, update res to include the current number in the possible sums
            res += num
        
        # Return the result
        return res
