from collections import defaultdict

class Solution:
    def sameOccurrence(self, arr, x, y):
        # Dictionary to store the frequency of each count_diff
        count_diff_map = defaultdict(int)
        
        # Initialize with a count_diff of 0, to handle cases where a valid subarray starts from the beginning
        count_diff_map[0] = 1

        count_diff = 0  # Difference between counts of x and y
        result = 0  # Number of valid subarrays

        for num in arr:
            # Update the count_diff based on the current element
            if num == x:
                count_diff += 1
            elif num == y:
                count_diff -= 1

            # If the current count_diff has been seen before,
            # it means there are valid subarrays ending at this position.
            result += count_diff_map[count_diff]

            # Update the count_diff_map with the current count_diff
            count_diff_map[count_diff] += 1

        return result
