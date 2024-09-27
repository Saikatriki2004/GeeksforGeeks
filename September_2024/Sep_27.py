#User function Template for python3

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,k,arr):
        
        # Create a deque to store indices of elements in the current window
        dq = []

        # Process the first window of size k
        for i in range(k):
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)

        # Process the remaining windows
        result = []
        for i in range(k, len(arr)):
            result.append(arr[dq[0]])

            # Remove elements that are no longer in the current window
            while dq and dq[0] <= i - k:
                dq.pop(0)

            # Add the new element to the deque
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)

        result.append(arr[dq[0]])
        return result
