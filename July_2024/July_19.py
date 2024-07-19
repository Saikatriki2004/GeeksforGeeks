from bisect import bisect_left, insort

class Solution:
    def constructLowerArray(self, arr):
        result = []
        sorted_list = []
        
        # Traverse the array from right to left
        for num in reversed(arr):
            # Find the index of the first element greater than or equal to num
            index = bisect_left(sorted_list, num)
            # Append the index to the result (count of smaller elements on the right)
            result.append(index)
            # Insert the current element into the sorted list
            insort(sorted_list, num)
        
        # Reverse the result list since we traversed the array from right to left
        return result[::-1]

# Example usage
sol = Solution()
print(sol.constructLowerArray([12, 1, 2, 3, 0, 11, 4]))  # Output: [6, 1, 1, 1, 0, 1, 0]
print(sol.constructLowerArray([1, 2, 3, 4, 5]))          # Output: [0, 0, 0, 0, 0]
