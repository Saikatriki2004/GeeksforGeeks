class Solution:
    def smallestNumber(self, s: int, d: int) -> str:
        # If the sum is greater than the maximum possible sum with d digits, return -1
        if s > 9 * d:
            return "-1"
        
        # Initialize the result list with zeros
        result = [0] * d
        
        # Decrement sum and place digits from the end to the start
        for i in range(d - 1, -1, -1):
            # Assign the minimum possible value to the current digit
            if s > 9:
                result[i] = 9
                s -= 9
            else:
                result[i] = s
                s = 0
        
        # Ensure the first digit is non-zero by adjusting the smallest non-zero value
        if result[0] == 0:
            for i in range(1, d):
                if result[i] > 0:
                    result[i] -= 1
                    result[0] = 1
                    break
        
        # Convert the digits list to string and return
        return ''.join(map(str, result))

# Example usage
sol = Solution()
print(sol.smallestNumber(9, 2))  # Output: "18"
print(sol.smallestNumber(20, 3))  # Output: "299"
print(sol.smallestNumber(9, 1))  # Output: "9"
print(sol.smallestNumber(10, 2))  # Output: "19"
print(sol.smallestNumber(1, 6))  # Output: "100000"
