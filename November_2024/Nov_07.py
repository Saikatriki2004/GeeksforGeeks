class Solution:
    def findSplit(self, arr):
        total_sum = sum(arr)
        
        # If total_sum is not divisible by 3, we cannot split it into three equal parts
        if total_sum % 3 != 0:
            return [-1, -1]
        
        target_sum = total_sum // 3
        n = len(arr)
        part_sum = 0
        count = 0
        result = []
        
        # Traverse the array to find two indices where we can split into three parts
        for i in range(n):
            part_sum += arr[i]
            
            if part_sum == target_sum:
                result.append(i)
                count += 1
                part_sum = 0  # reset for the next segment
            
            # If we have found two indices to split, we are done
            if count == 2 and i < n - 1:
                return [result[0], result[1] + 1]
        
        # If we cannot find such split, return [-1, -1]
        return [-1, -1]
