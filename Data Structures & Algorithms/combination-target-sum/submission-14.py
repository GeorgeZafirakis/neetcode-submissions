class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n       = len(nums)
        res     = []

        def dfs(i,curSet,curSum):

            # Base Case
            if i >= n or curSum > target:
                return

            if curSum == target:
                res.append(curSet.copy())
                return

            # Recursive Case
            curSet.append(nums[i])
            dfs(i,curSet,curSum + nums[i])
            curSet.pop()
            dfs(i+1,curSet, curSum) 

        dfs(0,[],0)
        return res