class Solution:
    def rowWithMax1s(self, arr):
        if not arr or not arr[0]:
            return -1

        n = len(arr)
        m = len(arr[0])
        
        max_row_index = -1
        j = m - 1

        for i in range(n):
            while j >= 0 and arr[i][j] == 1:
                j -= 1
                max_row_index = i

        return max_row_index

# Example usage:
arr1 = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]
print(Solution().rowWithMax1s(arr1))  # Output: 2

arr2 = [
    [0, 0],
    [1, 1]
]
print(Solution().rowWithMax1s(arr2))  # Output: 1
