class Solution:
    def threeSumClosest(self, arr, target):
        # Step 1: Sort the array
        arr.sort()
        n = len(arr)
        closest_sum = float('inf')

        # Step 2: Use a nested loop with three pointers
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                # Step 3: Check if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                # If the same difference, but a higher sum, update the closest_sum
                elif abs(current_sum - target) == abs(closest_sum - target):
                    closest_sum = max(closest_sum, current_sum)

                # Step 4: Adjust the pointers
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
        
        return closest_sum

# Example usage
sol = Solution()
arr1 = [-7, 9, 8, 3, 1, 1]
target1 = 2
print(sol.threeSumClosest(arr1, target1))  # Output: 2

arr2 = [5, 2, 7, 5]
target2 = 13
print(sol.threeSumClosest(arr2, target2))  # Output: 14
