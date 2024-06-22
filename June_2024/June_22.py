class Solution:
    def ExtractNumber(self, sentence):
        # Split the sentence into words
        words = sentence.split()
        
        # Extract all words that are numbers
        numbers = [word for word in words if word.isdigit()]
        
        # Filter out numbers containing '9'
        valid_numbers = [int(number) for number in numbers if '9' not in number]
        
        # If there are no valid numbers, return -1
        if not valid_numbers:
            return -1
        
        # Return the maximum valid number
        return max(valid_numbers)

# Example usage:
solution = Solution()
print(solution.ExtractNumber("This is alpha 5057 and 97"))  # Output: 5057
print(solution.ExtractNumber("Another input 9007"))         # Output: -1
print(solution.ExtractNumber("Here we have 888, 777, and 123456"))  # Output: 123456
