class Solution:
    def search(self, pat, txt):
        # Initialize variables
        result = []
        pat_len = len(pat)
        txt_len = len(txt)
        
        # Loop through txt with a sliding window of size len(pat)
        for i in range(txt_len - pat_len + 1):
            # Extract substring and compare with pat
            if txt[i:i + pat_len] == pat:
                result.append(i)
        
        return result
