class Solution:
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        result = []
        i, j = 0, 0
        n, m = len(a), len(b)
        
        # Traverse both arrays
        while i < n and j < m:
            # Skip duplicates in result
            if result and result[-1] == a[i]:
                i += 1
                continue
            if result and result[-1] == b[j]:
                j += 1
                continue
            
            # Compare and add elements to result
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            elif a[i] > b[j]:
                result.append(b[j])
                j += 1
            else:
                result.append(a[i])
                i += 1
                j += 1
        
        # Add remaining elements from a
        while i < n:
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i += 1
        
        # Add remaining elements from b
        while j < m:
            if not result or result[-1] != b[j]:
                result.append(b[j])
            j += 1
        
        return result
