class Solution:
    def alternateSort(self, arr):
        # Step 1: Sort the array in ascending order
        arr.sort()

        n = len(arr)
        result = [0] * n  # Create a result array of the same size

        # Step 2: Use two pointers to fill the result array
        left = 0          # Pointer for the smallest elements
        right = n - 1     # Pointer for the largest elements

        # Step 3: Fill the result array by alternating largest and smallest elements
        for i in range(n):
            if i % 2 == 0:  # Even index -> largest element
                result[i] = arr[right]
                right -= 1
            else:           # Odd index -> smallest element
                result[i] = arr[left]
                left += 1

        return result
