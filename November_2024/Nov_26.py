def circularSubarraySum(arr):
    n = len(arr)
    
    # Helper function for standard Kadane's algorithm
    def kadane(nums):
        max_ending_here = max_so_far = nums[0]
        for num in nums[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Step 1: Find the max subarray sum using standard Kadane's algorithm
    max_kadane = kadane(arr)
    
    # Step 2: Find the max circular subarray sum
    total_sum = sum(arr)
    # Invert the array to find the min subarray sum
    for i in range(n):
        arr[i] = -arr[i]
    
    # Calculate the minimum subarray sum
    min_kadane = kadane(arr)
    
    # Restore the array
    for i in range(n):
        arr[i] = -arr[i]
    
    # The maximum circular sum is total sum minus the minimum subarray sum
    max_circular = total_sum + min_kadane  # Adding because we negated the array
    
    # If all numbers are negative, max_circular is not valid; use max_kadane
    if max_circular == 0:
        return max_kadane
    
    # Step 3: Return the maximum of the two
    return max(max_kadane, max_circular)
