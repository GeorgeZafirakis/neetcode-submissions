class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        if n == 0: return [[]]
        if n == 1: return intervals

        res = []
        intervals.sort()
        
        i = 0
        while i < n - 1:

            if intervals[i][1] < intervals[i+1][0]:
                res.append(intervals[i])
                i += 1
            else:
                newInterval = [
                    min(intervals[i][0],intervals[i+1][0]),
                    max(intervals[i][1],intervals[i+1][1])
                ]
                intervals[i] = newInterval
                intervals.remove(intervals[i+1])
                n -= 1

        res.append(intervals[-1])
        return res
