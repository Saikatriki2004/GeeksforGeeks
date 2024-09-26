class Solution:
    # Function to find maximum number of consecutive steps
    # to gain an increase in altitude with each step.
    def maxStep(self, arr):
        # Initialize variables to store the maximum and current step counts
        max_steps = 0
        current_steps = 0
        
        # Iterate through the array starting from the second element
        for i in range(1, len(arr)):
            # Check if the current building is taller than the previous one
            if arr[i] > arr[i - 1]:
                current_steps += 1  # Increment current step count
            else:
                current_steps = 0  # Reset current step count
            
            # Update the maximum steps encountered so far
            max_steps = max(max_steps, current_steps)
        
        return max_steps
