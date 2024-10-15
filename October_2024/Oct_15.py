class Solution:
    # Function to count the number of subarrays which add to the given sum.
    def subArraySum(self, arr, tar):
        # Hashmap to store the frequency of prefix sums
        prefix_sum_count = {}
        prefix_sum = 0  # This will hold the cumulative sum of elements
        count = 0  # To store the total number of subarrays that sum to tar

        # Initialize the hashmap with the prefix sum 0, which occurs once initially
        prefix_sum_count[0] = 1

        for num in arr:
            # Update the cumulative sum (prefix sum)
            prefix_sum += num

            # Check if there is a prefix sum that satisfies the condition
            if prefix_sum - tar in prefix_sum_count:
                # If yes, we found a subarray ending at the current index with sum tar
                count += prefix_sum_count[prefix_sum - tar]

            # Add the current prefix sum to the hashmap (or update its count)
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1
            else:
                prefix_sum_count[prefix_sum] = 1

        return count
