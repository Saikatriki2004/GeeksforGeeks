from typing import List

class Solution:
    def countFreq(self, arr: List[int], target: int) -> int:
        # Helper function to find the first occurrence of target
        def find_first(arr, target):
            left, right = 0, len(arr) - 1
            first = -1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    first = mid
                    right = mid - 1  # Move left to find earlier occurrences
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first
        
        # Helper function to find the last occurrence of target
        def find_last(arr, target):
            left, right = 0, len(arr) - 1
            last = -1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    last = mid
                    left = mid + 1  # Move right to find later occurrences
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last
        
        # Find first and last occurrences
        first = find_first(arr, target)
        if first == -1:
            return 0  # Target not found
        
        last = find_last(arr, target)
        return last - first + 1
