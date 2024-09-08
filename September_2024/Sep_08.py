class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n <= 1:
            return 0
        
        # If the first element is 0, it's not possible to jump anywhere
        if arr[0] == 0:
            return -1
        
        # maxReach: The farthest index that can be reached
        # step: The number of steps we can still take
        # jump: Number of jumps made so far
        maxReach = arr[0]
        step = arr[0]
        jump = 1
        
        for i in range(1, n):
            # Check if we've reached the end of the array
            if i == n - 1:
                return jump
            
            # Update maxReach with the farthest point that can be reached
            maxReach = max(maxReach, i + arr[i])
            
            # Use a step to move to the next index
            step -= 1
            
            # If no further steps remain, we must jump
            if step == 0:
                jump += 1
                
                # Check if the current index is within the maximum reach
                if i >= maxReach:
                    return -1
                
                # Re-initialize steps for the new jump
                step = maxReach - i
        
        return -1

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    print(sol.minJumps(arr))  # Output: 3
    
    arr = [1, 4, 3, 2, 6, 7]
    print(sol.minJumps(arr))  # Output: 2
