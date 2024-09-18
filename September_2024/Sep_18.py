class Solution:
    
    # Function to check if brackets are balanced or not.
    def ispar(self, x: str) -> bool:
        # Stack to hold opening brackets.
        stack = []
        
        # Dictionary to hold the pairs of brackets.
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
        # Traverse through the expression.
        for char in x:
            # If it's an opening bracket, push to stack.
            if char in bracket_map.values():
                stack.append(char)
            # If it's a closing bracket, check if it matches the top of the stack.
            elif char in bracket_map:
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False
        
        # If stack is empty, the brackets are balanced.
        return len(stack) == 0
# Test case 1
x = "[()]{}{[()()]()}"
print(Solution().ispar(x))  # Output: True

# Test case 2
x = "[(])"
print(Solution().ispar(x))  # Output: False
