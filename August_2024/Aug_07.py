#K-th element of two Arrays
class Solution:
    def kthElement(self, k, arr1, arr2):
        n, m = len(arr1), len(arr2)

        # Ensure arr1 is the smaller array for the binary search to be efficient
        if n > m:
            return self.kthElement(k, arr2, arr1)
        
        low, high = max(0, k - m), min(k, n)

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = k - mid1

            left1 = arr1[mid1 - 1] if mid1 > 0 else float('-inf')
            left2 = arr2[mid2 - 1] if mid2 > 0 else float('-inf')
            right1 = arr1[mid1] if mid1 < n else float('inf')
            right2 = arr2[mid2] if mid2 < m else float('inf')

            # Check if we have found the right partition
            if left1 <= right2 and left2 <= right1:
                return max(left1, left2)
            elif left1 > right2:
                high = mid1 - 1
            else:
                low = mid1 + 1

        return -1  # This case should not be reached if inputs are valid

# Example usage:
solution = Solution()
arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 5
print(solution.kthElement(k, arr1, arr2))  # Output: 6

arr1 = [100, 112, 256, 349, 770]
arr2 = [72, 86, 113, 119, 265, 445, 892]
k = 7
print(solution.kthElement(k, arr1, arr2))  # Output: 256
