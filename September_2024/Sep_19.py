class Solution:
    # Function to reverse words in a given string.
    def reverseWords(self, str):
        # Split the string by '.' and reverse the list of words.
        words = str.split('.')
        reversed_words = words[::-1]
        
        # Join the reversed list with '.' and return.
        return '.'.join(reversed_words)
# Create an instance of the Solution class
solution = Solution()

# Example 1
input_str1 = "i.like.this.program.very.much"
output1 = solution.reverseWords(input_str1)
print(f"Input: {input_str1}")
print(f"Output: {output1}")
# Expected Output: much.very.program.this.like.i

# Example 2
input_str2 = "pqr.mno"
output2 = solution.reverseWords(input_str2)
print(f"Input: {input_str2}")
print(f"Output: {output2}")
# Expected Output: mno.pqr
