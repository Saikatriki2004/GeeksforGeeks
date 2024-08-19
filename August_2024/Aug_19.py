import heapq

class Solution:
    def kthSmallest(self, arr, k):
        # Convert array into a min-heap
        heapq.heapify(arr)
        
        # Extract the smallest element k times
        for _ in range(k - 1):
            heapq.heappop(arr)
        
        # The root of the heap is now the kth smallest element
        return heapq.heappop(arr)
sol = Solution()
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(sol.kthSmallest(arr, k))  # Output: 7
