class Solution:
    def findMajority(self, nums):
        if not nums:
            return [-1]
        
        # Step 1: Find candidates that could potentially have more than n/3 votes
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Validate the candidates by counting their occurrences
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        # Step 3: Return the valid candidates or -1 if none are valid
        result = []
        n = len(nums)
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)
        
        return result if result else [-1]

# Example usage:
solution = Solution()
print(solution.findMajority([2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]))  # Output: [5, 6]
print(solution.findMajority([1, 2, 3, 4, 5]))                    # Output: [-1]
