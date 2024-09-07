# User function Template for python3

class Solution:
    def findNth(self, n: int) -> int:
        # Convert the number to a string and remove all '9's by treating it as base 9
        result = ""
        while n > 0:
            digit = n % 9  # Get the last digit in base 9
            result = str(digit) + result
            n //= 9
        
        return int(result)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    n = 10
    print(f"The {n}th number without a 9 is: {sol.findNth(n)}")  # Output: 11
    
    n = 15
    print(f"The {n}th number without a 9 is: {sol.findNth(n)}")  # Output: 16

    n = 25
    print(f"The {n}th number without a 9 is: {sol.findNth(n)}")  # Output: 28
