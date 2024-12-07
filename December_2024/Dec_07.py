class Solution:
    # Helper function to merge two halves and count inversions
    def merge_and_count(self, arr, temp_arr, left, mid, right):
        i = left    # Starting index for left subarray
        j = mid + 1 # Starting index for right subarray
        k = left    # Starting index to be sorted
        inv_count = 0
        
        # Merge the two subarrays
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                # There are mid - i inversions because all elements in the left subarray
                # (arr[i] to arr[mid]) are greater than arr[j]
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1

        # Copy the remaining elements of the left subarray, if any
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        # Copy the remaining elements of the right subarray, if any
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        # Copy the sorted subarray into the original array
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]
        
        return inv_count

    # Function to use modified merge sort to count inversions
    def merge_sort_and_count(self, arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2

            # Count inversions in the left subarray
            inv_count += self.merge_sort_and_count(arr, temp_arr, left, mid)

            # Count inversions in the right subarray
            inv_count += self.merge_sort_and_count(arr, temp_arr, mid + 1, right)

            # Count split inversions
            inv_count += self.merge_and_count(arr, temp_arr, left, mid, right)
        
        return inv_count

    # Function to count inversions in the array
    def inversionCount(self, arr):
        n = len(arr)
        temp_arr = [0] * n
        return self.merge_sort_and_count(arr, temp_arr, 0, n - 1)
