class Solution:
    def minChar(self, s):
        # Reverse the string
        reversed_s = s[::-1]
        
        # Combine the string with a delimiter
        combined = s + '#' + reversed_s
        
        # Compute the LPS array
        n = len(combined)
        lps = [0] * n
        j = 0  # Length of previous LPS
        
        for i in range(1, n):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j
        
        # Minimum characters to add
        return len(s) - lps[-1]
