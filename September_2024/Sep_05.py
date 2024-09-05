# Define the solution class
class Solution:
    def missingNumber(self, n, arr):
        # Calculate the sum of the first n natural numbers
        total_sum = n * (n + 1) // 2
        
        # Calculate the sum of the elements in the array
        array_sum = sum(arr)
        
        # The missing number is the difference between the total sum and array sum
        return total_sum - array_sum

# Example test case
if __name__ == "__main__":
    # Creating an instance of Solution
    sol = Solution()
    
    # Given array of size n-1 and n
    arr = [1, 2, 3, 5]  # Missing 4
    n = 5
    
    # Finding the missing number
    missing = sol.missingNumber(n, arr)
    
    # Print the result
    print(f"The missing number is: {missing}")
