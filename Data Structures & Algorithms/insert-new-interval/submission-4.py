class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        for i in range(len(intervals)):

            # New interval before current interval
            # Add new interval and exit
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # New interval after current interval
            elif newInterval[0] > intervals[i][1]:
                # Edge Case, check res length and add newInterval if needed
                res.append(intervals[i])
                continue
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]


        # If not inserted yet, add it at the end
        res.append(newInterval)
        return res
            