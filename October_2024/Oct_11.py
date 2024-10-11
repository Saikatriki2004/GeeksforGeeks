class Solution:
    def rearrange(self, arr):
        n = len(arr)
        
        for i in range(n):
            # Keep swapping until arr[i] is in its correct position or arr[i] is -1 or out of bounds
            while 0 <= arr[i] < n and arr[i] != i and arr[i] != arr[arr[i]]:
                # Swap arr[i] with arr[arr[i]]
                arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        
        # Now place -1 at positions where the element is not in the correct place
        for i in range(n):
            if arr[i] != i:
                arr[i] = -1
        
        return arr
