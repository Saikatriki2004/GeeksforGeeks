class Solution:
    # Function to find the maximum occurred integer in all ranges.
    def maxOccured(self, n, l, r, maxx):
        # Initialize the frequency array
        freq = [0] * (maxx + 2)
        
        # Mark the frequency changes at the start and end+1 positions
        for i in range(n):
            freq[l[i]] += 1
            freq[r[i] + 1] -= 1
        
        # Calculate the prefix sum to determine the actual frequencies
        max_count = freq[0]
        max_value = 0
        
        for i in range(1, maxx + 1):
            freq[i] += freq[i - 1]
            if freq[i] > max_count:
                max_count = freq[i]
                max_value = i
        
        return max_value

# Example usage:
solution = Solution()

n = 4
l = [1, 4, 3, 1]
r = [15, 8, 5, 4]
maxx = 15
print(solution.maxOccured(n, l, r, maxx))  # Output: 4

n = 5
l = [1, 5, 9, 13, 21]
r = [15, 8, 12, 20, 30]
maxx = 30
print(solution.maxOccured(n, l, r, maxx))  # Output: 5
