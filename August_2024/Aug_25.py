class Solution:
    def countPairs(self, arr, brr):
        def count(x):
            # Function to count the number of y's where x^y > y^x
            if x == 0:
                return 0
            if x == 1:
                return count_0
            # Count pairs where x^y > y^x for y > 1
            count = len(brr) - binary_search(x)
            count += count_1  # All pairs (x, 1) are valid because x^1 > 1^x
            
            # Adjustments for specific x values
            if x == 2:
                count -= count_3  # 2^3 <= 3^2
                count -= count_4  # 2^4 <= 4^2
            if x == 3:
                count += count_2  # 3^2 > 2^3
            
            return count

        def binary_search(val):
            # Function to find the first index of the element in brr that is greater than `val`
            low, high = 0, len(brr)
            while low < high:
                mid = (low + high) // 2
                if brr[mid] > val:
                    high = mid
                else:
                    low = mid + 1
            return low

        brr.sort()
        count_0 = brr.count(0)
        count_1 = brr.count(1)
        count_2 = brr.count(2)
        count_3 = brr.count(3)
        count_4 = brr.count(4)

        total_pairs = 0
        for x in arr:
            total_pairs += count(x)

        return total_pairs

# Example usage:
solution = Solution()
arr = [2, 1, 6]
brr = [1, 5]
print(solution.countPairs(arr, brr))  # Expected output: 3
