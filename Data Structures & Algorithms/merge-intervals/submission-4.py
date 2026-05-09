class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []
        
        res = []
        sortedIntervals = sorted(intervals, key = lambda x: x[0])

        for i in range(len(sortedIntervals) - 1):
            
            if sortedIntervals[i][1] < sortedIntervals[i+1][0]:
                res.append(sortedIntervals[i])

            if sortedIntervals[i][1] >= sortedIntervals[i+1][0]:
                sortedIntervals[i+1] = [
                    min(sortedIntervals[i][0], sortedIntervals[i+1][0]),
                    max(sortedIntervals[i][1], sortedIntervals[i+1][1])
                ]

        res.append(sortedIntervals[-1])
        return res