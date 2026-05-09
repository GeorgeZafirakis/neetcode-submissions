class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:

            h       = min(heights[l], heights[r])
            width   = r - l
            area    = h * width
            maxArea = max(area, maxArea)

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l +=1 


        return maxArea

        