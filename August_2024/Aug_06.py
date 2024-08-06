#Validate an IP Address
class Solution:
    def isValid(self, s):
        # Split the string by the '.' delimiter
        parts = s.split('.')
        
        # An IPv4 address must have exactly 4 parts
        if len(parts) != 4:
            return False
        
        # Check each part
        for part in parts:
            # Each part must be non-empty, consist of digits only, and have no leading zeros
            if len(part) == 0 or not part.isdigit() or (len(part) > 1 and part[0] == '0'):
                return False
            
            # Convert part to an integer and check if it's within the valid range
            if not 0 <= int(part) <= 255:
                return False
        
        # All checks passed, the IP is valid
        return True

# Example usage:
solution = Solution()

# Test cases
print(solution.isValid("222.111.111.111"))  # Output: True
print(solution.isValid("5555..555"))        # Output: False
print(solution.isValid("0.0.0.0"))          # Output: True
print(solution.isValid("256.256.256.256"))  # Output: False
print(solution.isValid("192.168.1.01"))     # Output: False (leading zero issue)
