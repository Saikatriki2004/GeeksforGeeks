class Solution:
    def peakElement(self, arr):
        n = len(arr)

        # Binary search for the peak element
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            # Check if mid is a peak element
            left = arr[mid - 1] if mid > 0 else float('-inf')
            right = arr[mid + 1] if mid < n - 1 else float('-inf')

            if arr[mid] > left and arr[mid] > right:
                return mid  # Return the index of the peak element

            # If the left neighbor is greater, move to the left half
            elif left > arr[mid]:
                high = mid - 1

            # Otherwise, move to the right half
            else:
                low = mid + 1

        return -1  # This case should not occur if the array is valid

# Example usage
arr = [10, 20, 15, 2, 23, 90, 80]
solution = Solution()
peak_index = solution.peakElement(arr)
# Verify the result
is_peak = False
if 0 <= peak_index < len(arr):
    left = arr[peak_index - 1] if peak_index > 0 else float('-inf')
    right = arr[peak_index + 1] if peak_index < len(arr) - 1 else float('-inf')
    is_peak = arr[peak_index] > left and arr[peak_index] > right

print(is_peak)  # Should print True
