class Solution:
    def binaryNextNumber(self, s: str) -> str:
        # Step 1: Convert binary string to decimal
        decimal_number = int(s, 2)
        
        # Step 2: Increment the decimal number by 1
        incremented_number = decimal_number + 1
        
        # Step 3: Convert the incremented number back to binary string
        binary_string = bin(incremented_number)[2:]
        
        return binary_string

# Example usage:
sol = Solution()
print(sol.binaryNextNumber("10"))  # Output: "11"
print(sol.binaryNextNumber("111")) # Output: "1000"
