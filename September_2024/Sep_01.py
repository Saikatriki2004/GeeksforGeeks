class Solution:
    def maxPathSum(self, arr1, arr2):
        n, m = len(arr1), len(arr2)
        i, j = 0, 0
        
        sum1, sum2, result = 0, 0, 0
        
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
            else:
                # When arr1[i] == arr2[j], it's a common element
                result += max(sum1, sum2) + arr1[i]
                sum1, sum2 = 0, 0
                i += 1
                j += 1
        
        # Add remaining elements from arr1
        while i < n:
            sum1 += arr1[i]
            i += 1
        
        # Add remaining elements from arr2
        while j < m:
            sum2 += arr2[j]
            j += 1
        
        # Add the maximum of remaining sums
        result += max(sum1, sum2)
        
        return result

# Example usage:
solution = Solution()

arr1 = [2, 3, 7, 10, 12]
arr2 = [1, 5, 7, 8]
print(solution.maxPathSum(arr1, arr2))  # Expected Output: 35
