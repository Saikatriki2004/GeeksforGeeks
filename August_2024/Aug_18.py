class Solution:
    def canSplit(self, arr):
        total_sum = sum(arr)
        
        # If the total sum is odd, it's impossible to split into two equal parts
        if total_sum % 2 != 0:
            return False
        
        half_sum = total_sum // 2
        current_sum = 0
        
        # Iterate over the array to find if a split point exists
        for num in arr:
            current_sum += num
            if current_sum == half_sum:
                return True
        
        return False
 sol = Solution()
print(sol.canSplit([1, 2, 3, 5]))  # Output: True (1+2+3 = 6, 5 = 5+0)
print(sol.canSplit([1, 1, 3, 5]))  # Output: False
     
