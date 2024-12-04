class Solution:
    # Function to check if two strings are rotations of each other or not.
    def areRotations(self, s1, s2):
        # If lengths are not equal, they cannot be rotations
        if len(s1) != len(s2):
            return False
        
        # Concatenate s1 with itself
        temp = s1 + s1
        
        # Check if s2 is a substring of the concatenated string
        return s2 in temp
