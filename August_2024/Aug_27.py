class Solution:
    def findMaxDiff(self, arr):
        n = len(arr)
        left_smaller = [0] * n
        right_smaller = [0] * n
        stack = []
        
        # Find nearest smaller to the left
        for i in range(n):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            left_smaller[i] = stack[-1] if stack else 0
            stack.append(arr[i])
        
        stack.clear()
        
        # Find nearest smaller to the right
        for i in range(n-1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            right_smaller[i] = stack[-1] if stack else 0
            stack.append(arr[i])
        
        # Find the maximum absolute difference
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(left_smaller[i] - right_smaller[i]))
        
        return max_diff
# Example usage:
solution = Solution()
arr = [2, 1, 8, 5, 4]
print(solution.findMaxDiff(arr))  # Output: 4
