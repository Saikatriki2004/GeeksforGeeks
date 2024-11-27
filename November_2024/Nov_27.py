class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        
        # Step 1: Replace all numbers <= 0 or > n with n+1
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = n + 1
        
        # Step 2: Mark indices corresponding to the numbers in the range [1, n]
        for i in range(n):
            num = abs(arr[i])  # Take absolute value since we may have marked numbers
            if 1 <= num <= n:
                arr[num - 1] = -abs(arr[num - 1])  # Mark the index
        
        # Step 3: Find the first index with a positive value
        for i in range(n):
            if arr[i] > 0:
                return i + 1  # Missing number is i + 1
        
        # Step 4: If all numbers 1 to n are present, return n + 1
        return n + 1
