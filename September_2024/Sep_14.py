class Solution:
    def rearrange(self, arr):
        # Separate positive and negative numbers into two lists
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]
        
        # Initialize variables to track the current index of pos and neg lists
        pos_idx, neg_idx = 0, 0
        i = 0
        
        # Rearrange the elements, starting with positive numbers
        while pos_idx < len(pos) and neg_idx < len(neg):
            if i % 2 == 0:
                arr[i] = pos[pos_idx]
                pos_idx += 1
            else:
                arr[i] = neg[neg_idx]
                neg_idx += 1
            i += 1
        
        # If there are remaining positive numbers, append them
        while pos_idx < len(pos):
            arr[i] = pos[pos_idx]
            pos_idx += 1
            i += 1
        
        # If there are remaining negative numbers, append them
        while neg_idx < len(neg):
            arr[i] = neg[neg_idx]
            neg_idx += 1
            i += 1

        return arr
