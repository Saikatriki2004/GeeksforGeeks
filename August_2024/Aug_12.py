class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        n = len(arr1)  # Both arrays are of the same length
        
        # Pointers for arr1 and arr2
        i = 0
        j = 0
        
        # Since there are 2n elements, the middle elements are at indices n-1 and n
        mid1, mid2 = None, None
        
        # We need to find the (n-1)th and nth element in the merged array
        for count in range(n + 1):
            if i < n and (j >= n or arr1[i] <= arr2[j]):
                if count == n - 1:
                    mid1 = arr1[i]
                if count == n:
                    mid2 = arr1[i]
                i += 1
            else:
                if count == n - 1:
                    mid1 = arr2[j]
                if count == n:
                    mid2 = arr2[j]
                j += 1
        
        return mid1 + mid2

# Example usage:
sol = Solution()
print(sol.sum_of_middle_elements([1, 2, 4, 6, 10], [4, 5, 6, 9, 12]))  # Output: 11
print(sol.sum_of_middle_elements([1, 12, 15, 26, 38], [2, 13, 17, 30, 45]))  # Output: 32
