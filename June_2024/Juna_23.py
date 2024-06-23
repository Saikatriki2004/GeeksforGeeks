class Solution:
    def bracketNumbers(self, str):
        stack = []
        result = []
        counter = 0

        for char in str:
            if char == '(':
                counter += 1
                stack.append(counter)
                result.append(counter)
            elif char == ')':
                result.append(stack.pop())

        return result

# Example usage:
solution = Solution()
print(solution.bracketNumbers("(aa(bdc))p(dee)"))  # Output: [1, 2, 2, 1, 3, 3]
print(solution.bracketNumbers("(((()("))  # Output: [1, 2, 3, 4, 4, 5]
