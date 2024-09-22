class Solution:
    def lps(self, string):
        n = len(string)
        
        # Create the lps (longest prefix suffix) array of size n
        lps = [0] * n
        
        # Length of the previous longest prefix suffix
        length = 0
        
        # The loop starts from index 1 as lps[0] is always 0
        i = 1
        
        while i < n:
            if string[i] == string[length]:
                # Match found, increment length and set lps[i]
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # We don't increment i here
                    length = lps[length - 1]
                else:
                    # If length == 0, set lps[i] = 0 and move to next
                    lps[i] = 0
                    i += 1
        
        # The value at lps[n-1] will give the length of the longest proper prefix which is also a suffix
        return lps[-1]

# Example Usage
sol = Solution()
print(sol.lps("abab"))  # Output: 2
print(sol.lps("aaaa"))  # Output: 3
