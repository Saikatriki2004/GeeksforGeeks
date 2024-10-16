class Solution:
    def checkSorted(self, a):
        hash1 = {}

        for i in range(1, len(a)+1):
            hash1[a[i-1]] = i
        
        swap = 0
        for i in range(1, len(a)+1):
            if swap == 2 and i == len(a):
                return True
            if swap > 2:
                return False
            if a[i-1] != i:
                a[i-1], a[hash1[i]-1] = a[hash1[i]-1], a[i-1]
                swap += 1
        return not swap