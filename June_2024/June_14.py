class Solution:
    def armstrongNumber(self, n: int) -> str:
        # Extracting digits of the number
        hundreds = n // 100
        tens = (n // 10) % 10
        units = n % 10
        
        # Calculating the sum of the cubes of the digits
        sum_of_cubes = hundreds**3 + tens**3 + units**3
        
        # Checking if the sum of the cubes is equal to the number itself
        if sum_of_cubes == n:
            return "Yes"
        else:
            return "No"

# Example usage:
solution = Solution()

n = 153
print(solution.armstrongNumber(n))  # Output: Yes

n = 372
print(solution.armstrongNumber(n))  # Output: No

n = 371
print(solution.armstrongNumber(n))  # Output: Yes

n = 370
print(solution.armstrongNumber(n))  # Output: Yes
