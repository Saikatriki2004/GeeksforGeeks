class Solution:
    def addBinary(self, s1, s2):
        # Initialize pointers for s1 and s2
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        result = []
        
        # Traverse both strings from the end
        while i >= 0 or j >= 0 or carry:
            # Get the binary digit from s1 or 0 if index out of range
            bit1 = int(s1[i]) if i >= 0 else 0
            # Get the binary digit from s2 or 0 if index out of range
            bit2 = int(s2[j]) if j >= 0 else 0
            
            # Calculate the sum of bits and carry
            total = bit1 + bit2 + carry
            result.append(str(total % 2))  # Append the current bit (0 or 1)
            carry = total // 2  # Update carry
            
            # Move pointers
            i -= 1
            j -= 1
        
        # Reverse the result and join to form the output string
        # Use lstrip('0') to remove leading zeros (and handle the case of '0')
        return ''.join(result[::-1]).lstrip('0') or '0'
