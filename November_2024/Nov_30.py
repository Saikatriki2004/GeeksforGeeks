class Solution:
    
    # Function to check whether two strings are anagrams of each other or not.
    def areAnagrams(self, s1, s2):
        # If lengths are not equal, they can't be anagrams
        if len(s1) != len(s2):
            return False
        
        # Use a frequency counter for both strings
        freq_s1 = {}
        freq_s2 = {}
        
        # Count characters in s1
        for char in s1:
            freq_s1[char] = freq_s1.get(char, 0) + 1
        
        # Count characters in s2
        for char in s2:
            freq_s2[char] = freq_s2.get(char, 0) + 1
        
        # Compare the frequency dictionaries
        return freq_s1 == freq_s2
