class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        low, mid, high = 0, 0, len(arr) - 1
        
        while mid <= high:
            if arr[mid] == 0:
                # Swap current element with low boundary
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # Leave as is and move mid
                mid += 1
            else:  # arr[mid] == 2
                # Swap current element with high boundary
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        
        return arr
