class Solution:
    def mergeArrays(self, a, b):
        n, m = len(a), len(b)
        gap = (n + m + 1) // 2  # Initial gap size

        while gap > 0:
            i = 0  # Pointer for the first array
            j = gap  # Pointer for comparing

            while j < (n + m):
                if j < n:  # Both pointers in the first array
                    if a[i] > a[j]:
                        a[i], a[j] = a[j], a[i]
                elif i < n:  # i in 'a', j in 'b'
                    if a[i] > b[j - n]:
                        a[i], b[j - n] = b[j - n], a[i]
                else:  # Both pointers in the second array
                    if b[i - n] > b[j - n]:
                        b[i - n], b[j - n] = b[j - n], b[i - n]
                i += 1
                j += 1

            # Update gap for the next iteration
            if gap == 1:
                break
            gap = (gap + 1) // 2

        return a, b

# Example Usage
solution = Solution()
a = [2, 4, 7, 10]
b = [2, 3]
print(solution.mergeArrays(a, b))  # Output: ([2, 2, 3, 4], [7, 10])
