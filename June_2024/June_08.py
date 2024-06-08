class Solution:
    def findExtra(self, n, a, b):
        low, high = 0, n - 2
        
        while low <= high:
            mid = (low + high) // 2
            
            # Compare the middle elements of a and b
            if a[mid] == b[mid]:
                # The extra element is in the right half
                low = mid + 1
            else:
                # The extra element is in the left half
                high = mid - 1
        
        # The 'low' index will be at the position of the extra element
        return low

# Example usage:
solution = Solution()

n = 7
arr1 = [2, 4, 6, 8, 9, 10, 12]
arr2 = [2, 4, 6, 8, 10, 12]
print(solution.findExtra(n, arr1, arr2))  # Output: 4

n = 6
arr1 = [3, 5, 7, 8, 11, 13]
arr2 = [3, 5, 7, 11, 13]
print(solution.findExtra(n, arr1, arr2))  # Output: 3
