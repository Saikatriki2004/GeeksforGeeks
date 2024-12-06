class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        # Sort the citations in descending order
        citations.sort(reverse=True)
        
        # Iterate and find the largest H-index
        h_index = 0
        for i, c in enumerate(citations):
            # Check if the current citation count satisfies the H-index condition
            if c >= i + 1:
                h_index = i + 1
            else:
                break
        
        return h_index
