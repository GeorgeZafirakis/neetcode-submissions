"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted([i.start for i in intervals])
        end   = sorted([i.end   for i in intervals])

        res           = 0
        openN, closeN = 0, 0

        while(openN) < len(intervals):

            if start[openN] < end[closeN]:
                openN += 1
            else:
                closeN += 1

            res = max(res, (openN - closeN))

        return res
            
        

