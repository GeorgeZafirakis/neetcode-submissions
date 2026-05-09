class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = []

        i = 0
        while i < len(intervals) - 1:          
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1] = [
                    min(intervals[i][0], intervals[i+1][0]),
                    max(intervals[i][1], intervals[i+1][1])
                    ]
                intervals[i]   = [-1] # Deletion flag 
            i += 1

        for interval in intervals:
            if interval != [-1]:
                res.append(interval)
        return res