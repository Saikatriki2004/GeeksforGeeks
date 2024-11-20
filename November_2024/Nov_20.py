class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n = len(arr)
        ans = []
        d = {}
        for i in arr:
            d[i] = 1+d.get(i,0)
        for i in d:
            if(d[i]>(n/3)):
                ans.append(i)
        ans.sort()
        return ans
