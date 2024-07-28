#Remove Duplicates
class Solution:
    def removeDups(self, str):
        seen = set()
        result = []

        for char in str:
            if char not in seen:
                seen.add(char)
                result.append(char)
        
        return ''.join(result)

# Example usage:
solution = Solution()
print(solution.removeDups("zvvo"))  # Output: "zvo"
print(solution.removeDups("gfg"))   # Output: "gf"
print(solution.removeDups("aabccdee"))  # Output: "abcde"
