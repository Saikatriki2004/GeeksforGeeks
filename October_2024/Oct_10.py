class Solution:
    def maxDistance(self, arr):
        first_occurrence = {}
        max_distance = 0
        
        # Traverse the array
        for i in range(len(arr)):
            if arr[i] in first_occurrence:
                # Calculate the distance and update max_distance if necessary
                max_distance = max(max_distance, i - first_occurrence[arr[i]])
            else:
                # Store the first occurrence of the element
                first_occurrence[arr[i]] = i
        
        return max_distance
