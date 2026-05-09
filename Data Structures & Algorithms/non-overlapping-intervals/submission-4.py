class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        res = 0
        intervals.sort()
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:

            # No overlap
            if start >= prevEnd:
                prevEnd = end
            # Overlap -> Get rid of longer interval
            else:
                prevEnd = min(prevEnd, end)
                res += 1
                
        return res

        
            
        