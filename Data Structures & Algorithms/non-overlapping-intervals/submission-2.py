class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0

        for start, end in intervals[1:]:
            # No overlapping
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                # Delete interval with "greated" end
                prevEnd = min(prevEnd, end)
        return res