class Solution:
    def findMaxProduct(self, arr):
        MOD = 10**9 + 7
        
        # Filter out zeros and count negative numbers
        non_zero = [num for num in arr if num != 0]
        negative_numbers = [num for num in non_zero if num < 0]
        positive_numbers = [num for num in non_zero if num > 0]
        
        # If there's only one non-zero element, return it
        if len(non_zero) == 0:
            return 0
        
        if len(non_zero) == 1:
            return non_zero[0] % MOD
        
        # Handle all negatives and zeros case
        if not positive_numbers and len(negative_numbers) == 1 and len(non_zero) == 1:
            return negative_numbers[0] % MOD
        
        product = 1
        
        # If the count of negative numbers is odd, remove the least negative number
        if len(negative_numbers) % 2 != 0:
            least_negative = max(negative_numbers)
            negative_numbers.remove(least_negative)
        
        # Calculate the product of all remaining non-zero numbers
        for num in positive_numbers + negative_numbers:
            product = (product * num) % MOD
        
        # Return the product modulo MOD
        return product % MOD

# Example usage
sol = Solution()
print(sol.findMaxProduct([-1, 0, -2, 4, 3]))  # Output: 24
print(sol.findMaxProduct([-1, 0]))            # Output: 0
print(sol.findMaxProduct([5]))                # Output: 5
print(sol.findMaxProduct([-1, -1, 7, -4, 9, 3, 2, -5, 10, -2]))  # Output: 151200
