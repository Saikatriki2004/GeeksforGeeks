class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # Initialize pointers
        low = 0
        mid = 0
        high = len(arr) - 1
        
        # Traverse the array and sort it
        while mid <= high:
            if arr[mid] == 0:
                # Swap arr[low] and arr[mid], and increment both low and mid
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # Move to the next element if it's 1
                mid += 1
            else:
                # Swap arr[mid] and arr[high], and decrement high
                arr[high], arr[mid] = arr[mid], arr[high]
                high -= 1
        
        return arr

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    arr = [0, 1, 2, 1, 0, 2, 1, 2, 0]
    print("Sorted array:", sol.sort012(arr))
