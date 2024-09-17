class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0

        arr.sort()

        ans = arr[-1] - arr[0]

        for i in range(1, n):
            if arr[i] - k < 0:
                continue

            maxi = max(arr[i - 1] + k, arr[-1] - k)
            mini = min(arr[0] + k, arr[i] - k)

            ans = min(ans, maxi - mini)

        return ans
