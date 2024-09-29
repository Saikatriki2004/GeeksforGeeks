class Solution:
    def totalCount(self, k, arr):
        total_count = 0
        for num in arr:
            total_count += (num + k - 1) // k
        return total_count
