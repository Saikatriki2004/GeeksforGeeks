#Maximize Array Value After Rearrangement:
class Solution:
    def Maximize(self, a): 
        # Modulus value as per the problem statement
        MOD = 10**9 + 7
        
        # Step 1: Sort the array
        a.sort()
        
        # Step 2: Calculate the sum of a[i] * i
        max_value = 0
        for i in range(len(a)):
            max_value = (max_value + a[i] * i) % MOD
        
        # Step 3: Return the computed value
        return max_value

# Example usage:
solution = Solution()
print(solution.Maximize([5, 3, 2, 4, 1]))  # Output: 40
print(solution.Maximize([1, 2, 3]))        # Output: 8
