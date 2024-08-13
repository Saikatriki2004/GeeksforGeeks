class Solution:
    def floorSqrt(self, n): 
        if n == 0 or n == 1:
            return n
        
        low, high = 1, n
        answer = 1
        
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            
            if square == n:
                return mid
            elif square < n:
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return answer

# Example usage:
sol = Solution()
print(sol.floorSqrt(5))  # Output: 2
print(sol.floorSqrt(4))  # Output: 2
print(sol.floorSqrt(10))  # Output: 3
print(sol.floorSqrt(16))  # Output: 4
