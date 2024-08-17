class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        
        # Initialize the left and right product arrays
        left_products = [1] * n
        right_products = [1] * n
        output = [1] * n
        
        # Compute left_products
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]
        
        # Compute right_products
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]
        
        # Construct the output array
        for i in range(n):
            output[i] = left_products[i] * right_products[i]
        
        return output

# Example usage:
sol = Solution()
print(sol.productExceptSelf([10, 3, 5, 6, 2]))  # Output: [180, 600, 360, 300, 900]
print(sol.productExceptSelf([12, 0]))           # Output: [0, 12]
