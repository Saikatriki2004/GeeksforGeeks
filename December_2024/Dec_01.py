class Solution:
    # Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self, s):
        # Step 1: Count frequencies of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Step 2: Find the first character with frequency 1
        for char in s:
            if char_count[char] == 1:
                return char
        
        # Step 3: If no non-repeating character, return '$'
        return '$'
