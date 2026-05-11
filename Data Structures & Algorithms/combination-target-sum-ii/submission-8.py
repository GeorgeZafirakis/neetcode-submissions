class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(candidates)
        res = []

        def dfs(i,subSet,curSum):

            # Base Case
            if curSum == target:
                res.append(subSet.copy())
                return

            if curSum > target:
                return

            if i >= len(nums):
                return

            # Recursive Case
            subSet.append(nums[i])
            dfs(i+1,subSet,curSum + nums[i])
            subSet.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1,subSet,curSum)
            return


        dfs(0,[],0)
        return res