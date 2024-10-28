class Solution:
    def removeDuplicates(self, arr):
        seen = set()  # To keep track of encountered elements
        result = []   # To store the output array without duplicates

        for num in arr:
            if num not in seen:  # If it's the first occurrence of num
                seen.add(num)     # Mark it as seen
                result.append(num)  # Add to the result

        return result
