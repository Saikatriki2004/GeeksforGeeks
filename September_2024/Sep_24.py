from collections import defaultdict

class Solution:
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return "-1"
        
        # Frequency map for characters in p
        freq_p = defaultdict(int)
        for char in p:
            freq_p[char] += 1
        
        # Sliding window
        start = 0
        min_len = float('inf')
        min_start = 0
        count = 0
        freq_window = defaultdict(int)
        
        for end in range(len(s)):
            # Include current character in window
            freq_window[s[end]] += 1
            
            # If this character is part of p and its frequency in window is less than or equal to required frequency
            if s[end] in freq_p and freq_window[s[end]] <= freq_p[s[end]]:
                count += 1
            
            # When all characters are matched
            while count == len(p):
                # Update the smallest window
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    min_start = start
                
                # Try to shrink the window by moving the start pointer
                freq_window[s[start]] -= 1
                if s[start] in freq_p and freq_window[s[start]] < freq_p[s[start]]:
                    count -= 1
                start += 1
        
        # If no window is found
        if min_len == float('inf'):
            return "-1"
        
        # Return the smallest window
        return s[min_start:min_start + min_len]
