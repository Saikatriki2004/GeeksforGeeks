#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        # Your code here
        from collections import defaultdict
        n = len(arr)
        def collect(i):
            target, m = -arr[i], defaultdict(list)
            for j in range(i+1, n):
                if target - arr[j] in m:
                    for idx in m[target-arr[j]]:
                        yield i, idx, j
                m[arr[j]].append(j)
        for i in range(n):
            yield from collect(i)
