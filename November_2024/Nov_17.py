class Solution:
    def reverseArray(self, arr):
        # Initialize two pointers
        left, right = 0, len(arr) - 1
        
        # Swap elements while left < right
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return arr  # Return the reversed array
