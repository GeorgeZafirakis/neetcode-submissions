class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res= []

        def dfs(nums, i, curList):

            # Base Case
            if i >= len(nums):
                res.append(curList.copy())
                return

            # Recursive Case
            curList.append(nums[i])
            dfs(nums,i+1,curList)
            curList.pop()
            dfs(nums,i+1,curList)

        dfs(nums,0,[])
        return res