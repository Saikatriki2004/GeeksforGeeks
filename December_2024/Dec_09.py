#User function Template for python3

class Solution:
    def insertInterval(self, intervals, newInterval):
        res = []
        i = 0
        n = len(intervals)
    
        # add non overlapping before new one
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
    
        # merge overlapping
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        res.append(newInterval)
        
        # add non overlapping after new ones
        while i < n:
            res.append(intervals[i])
            i += 1
    
        return res
