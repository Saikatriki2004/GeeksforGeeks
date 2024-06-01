class Solution:
    def oddEven(self, s: str) -> str:
        # Frequency dictionary to count occurrences of each character
        frequency = {}
        
        # Fill frequency dictionary
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        
        # Initialize counters for x and y
        x = 0
        y = 0
        
        # Check each character and its frequency
        for char, count in frequency.items():
            # Get position in alphabet (1-based index)
            position = ord(char) - ord('a') + 1
            
            # Check for even position and even frequency
            if position % 2 == 0 and count % 2 == 0:
                x += 1
            # Check for odd position and odd frequency
            elif position % 2 == 1 and count % 2 == 1:
                y += 1
        
        # Sum x and y and check if it's even or odd
        if (x + y) % 2 == 0:
            return "EVEN"
        else:
            return "ODD"

# Example usage:
solution = Solution()
print(solution.oddEven("abbbcc"))  # Output: ODD
print(solution.oddEven("nobitaa")) # Output: EVEN
