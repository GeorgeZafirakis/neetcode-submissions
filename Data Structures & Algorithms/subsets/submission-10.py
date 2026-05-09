class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(i, curList):

            # Base Case
            if i >= len(nums):
                res.append(curList.copy())
                return

            # Recursive Case
            curList.append(nums[i])
            dfs(i+1, curList)
            curList.pop()
            dfs(i+1, curList)

        dfs(0, [])
        return res