import heapq
from typing import List

class Solution:
    # Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr: List[int]) -> int:
        # Base case: If there's only one rope, no cost is incurred.
        if len(arr) == 1:
            return 0
        
        # Create a min-heap from the list of ropes
        heapq.heapify(arr)
        
        total_cost = 0
        
        # Continue combining ropes until one remains
        while len(arr) > 1:
            # Extract the two smallest ropes
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            
            # The cost of combining them is the sum of their lengths
            combined_cost = first + second
            
            # Add the combined rope back into the heap
            heapq.heappush(arr, combined_cost)
            
            # Add the cost to the total
            total_cost += combined_cost
        
        return total_cost
