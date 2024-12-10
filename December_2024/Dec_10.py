class Solution:
    def minRemoval(self, intervals):
        # Step 1: Sort intervals based on the end time
        intervals.sort(key=lambda x: x[1])
        
        # Step 2: Initialize variables
        prev_end = float('-inf')  # Tracks the end time of the last non-overlapping interval
        removals = 0             # Count of intervals to remove
        
        # Step 3: Iterate over sorted intervals
        for start, end in intervals:
            if start < prev_end:
                # Overlap detected, we need to remove this interval
                removals += 1
            else:
                # No overlap, update prev_end
                prev_end = end
        
        return removals
