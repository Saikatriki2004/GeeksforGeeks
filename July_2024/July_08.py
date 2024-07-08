class Solution:
    def search(self, arr, key):
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            # If the key is found
            if arr[mid] == key:
                return mid

            # Check if the left half is sorted
            if arr[left] <= arr[mid]:
                # If the key is in the range of the sorted left half
                if arr[left] <= key < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # The right half must be sorted
            else:
                # If the key is in the range of the sorted right half
                if arr[mid] < key <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # If the key is not found
        return -1

# Example usage
sol = Solution()

arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key1 = 10
print(sol.search(arr1, key1))  # Output: 5

arr2 = [3, 5, 1, 2]
key2 = 6
print(sol.search(arr2, key2))  # Output: -1
