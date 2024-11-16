class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        j = 0  # Pointer for placing the next non-zero element
        
        # Traverse the array
        for i in range(n):
            if arr[i] != 0:
                # Swap the non-zero element with the element at index j
                arr[i], arr[j] = arr[j], arr[i]
                j += 1  # Increment the pointer for non-zero elements
