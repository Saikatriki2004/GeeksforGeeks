from collections import Counter

class Solution:
    def countPairsWithDiffK(self, arr, k):
        count = 0
        freq = Counter(arr)  # Count frequencies of elements

        for num in freq:
            # Check if num + k exists
            if (num + k) in freq:
                count += freq[num] * freq[num + k]  # Count all valid pairs

        return count
