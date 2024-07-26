class Solution:
    def kPangram(self, string: str, k: int) -> bool:
        # Create a set of unique alphabetic characters from the string
        present_letters = set(c for c in string if c.isalpha())
        
        # Calculate the number of unique alphabetic characters present
        num_unique_letters = len(present_letters)
        
        # Number of missing letters to make the string a pangram
        missing_letters = 26 - num_unique_letters
        
        # If all 26 letters are present, no operations are needed
        if missing_letters <= 0:
            return True
        
        # Total number of alphabetic characters in the string
        total_alphabetic_chars = sum(1 for c in string if c.isalpha())
        
        # Check if the number of missing letters can be covered by k operations
        # and ensure we have enough characters to replace
        return missing_letters <= k and total_alphabetic_chars >= 26

# Example usage
sol = Solution()
print(sol.kPangram("the quick brown fox jumps over the lazy dog", 0))  # Output: True
print(sol.kPangram("aaaaaaaaaaaaaaaaaaaaaaaaaa", 25))  # Output: True
print(sol.kPangram("a b c d e f g h i j k l m", 20))  # Output: False
