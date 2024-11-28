class Solution:
    def myAtoi(self, s):
        # Step 1: Initialize variables
        i = 0
        n = len(s)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 2: Ignore leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 3: Handle sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 4: Convert characters to integer
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')  # Convert char to digit
            result = result * 10 + digit
            
            # Check for overflow
            if result * sign > INT_MAX:
                return INT_MAX
            if result * sign < INT_MIN:
                return INT_MIN
            
            i += 1
        
        # Step 5: Apply sign and return
        return result * sign
