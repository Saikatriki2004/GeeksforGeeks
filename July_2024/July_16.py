#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
		# Initialize the occurrence counter
        occurrence = 0
        
        # Iterate through the string
        for i in range(len(s)):
            # If the current character matches `ch`, increment the occurrence counter
            if s[i] == ch:
                occurrence += 1
            
            # If the occurrence counter matches `count`, return the substring from the next character
            if occurrence == count:
                return s[i+1:]
        
        # If the loop ends and we haven't found the `count`-th occurrence, return an empty string
        return ""
# Example usage
sol = Solution()
print(sol.getSubstringAfterCount("Thisisdemostring", 'i', 3))  # Output: "ng"
print(sol.getSubstringAfterCount("Thisisdemostri", 'i', 3))    # Output: ""
print(sol.getSubstringAfterCount("abcd", 'x', 2))              # Output: ""
