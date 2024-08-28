from collections import Counter

class Solution:
    def sortByFreq(self, arr):
        # Step 1: Calculate the frequency of each element
        freq = Counter(arr)
        
        # Step 2: Sort based on frequency first (in descending order), then by value (in ascending order)
        sorted_arr = sorted(arr, key=lambda x: (-freq[x], x))
        
        return sorted_arr
solution = Solution()
arr = [4, 5, 6, 5, 4, 3]
result = solution.sortByFreq(arr)
print(result)  # Output: [4, 4, 5, 5, 3, 6]
