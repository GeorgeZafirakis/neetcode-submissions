class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []

        res = []
        intervals.sort()
        res.append(intervals[0])

        for start, end in intervals:

            if res[-1][1] < start:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)

        return res