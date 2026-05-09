class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = []
        i = 0

        while i < len(intervals):
            
            start, end = intervals[i]

            # Merge all overlapping intervals
            while i + 1 < len(intervals) and intervals[i + 1][0] <= end:
                end = max(end, intervals[i + 1][1])
                i += 1

            res.append([start, end])
            i += 1

        return res



# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
#         res = []
#         intervals.sort()
#         i = 0

#         while i < len(intervals):

#             newInterval = []
#             if i + 1 < len(intervals) and (intervals[i][1] <= intervals[i+1][0] or intervals[i+1][0] >= intervals[i][1]):
                
#                 while i + 1 < len(intervals) and (intervals[i][1] <= intervals[i+1][0] or intervals[i+1][0] >= intervals[i][1]):
#                     newInterval = [
#                         min(intervals[i][0],intervals[i+1][0]),
#                         max(intervals[i][1],intervals[i+1][1])
#                     ]
#                     i += 1
#                 res.append(newInterval)
#             else:
#                 res.append(intervals[i])
#                 i += 1
#         return res
