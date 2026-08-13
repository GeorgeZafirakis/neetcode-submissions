class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(i,curList):

            if i >= len(nums):
                res.append(curList.copy())
                return

            curList.append(nums[i])
            dfs(i+1,curList)
            curList.pop()
            dfs(i+1, curList)
            return

        dfs(0,[])
        return res