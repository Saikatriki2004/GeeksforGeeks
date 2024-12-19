class Solution:
    def kthMissing(self, arr, k):
        # Binary search to find the kth missing number
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1

        return low + k  # Final position of the missing number

# Example usage
solution = Solution()
print(solution.kthMissing([2, 3, 4, 7, 11], 5))  # Output: 9
print(solution.kthMissing([1, 2, 3], 2))         # Output: 5
print(solution.kthMissing([3, 5, 9, 10, 11, 12], 2))  # Output: 2
