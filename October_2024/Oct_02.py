# from typing import List


class Solution:
    def rotateDelete(self,  arr):
        # code here
        n = len(arr)
        for i in range(1,n):
            arr.insert(0,arr.pop(-1))
            if len(arr) - i < 0:
                arr.pop(0)
            else:
                arr.pop(len(arr)-i)
        return arr[0]
