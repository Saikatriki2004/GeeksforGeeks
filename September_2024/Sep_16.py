class Solution:
    def maxLength(self, s: str) -> int:
        # Initialize a stack to store the indices
        stack = [-1]  # Start with -1 to handle edge cases
        max_len = 0
        
        # Traverse through the string
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of '(' onto the stack
                stack.append(i)
            else:
                # Pop from the stack if a closing bracket ')' is found
                stack.pop()
                
                # If stack is not empty, calculate the current length
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    # If stack is empty, push the current index as a new base
                    stack.append(i)
        
        return max_len

# Example usage:
sol = Solution()
print(sol.maxLength(")()())"))  # Output: 4
print(sol.maxLength("()(()"))   # Output: 2
