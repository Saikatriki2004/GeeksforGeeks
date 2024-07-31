class Solution:
    def longestCommonPrefix(self, arr):
        if not arr:
            return "-1"
        
        # Take the first string as the initial prefix
        prefix = arr[0]
        
        # Compare the prefix with each string in the array
        for string in arr[1:]:
            while string[:len(prefix)] != prefix and prefix:
                # Truncate the prefix
                prefix = prefix[:len(prefix)-1]
            if not prefix:
                return "-1"
        
        return prefix if prefix else "-1"

# Example usage:
sol = Solution()
print(sol.longestCommonPrefix(["geeksforgeeks", "geeks", "geek", "geezer"]))  # Output: "gee"
print(sol.longestCommonPrefix(["hello", "world"]))  # Output: "-1"
