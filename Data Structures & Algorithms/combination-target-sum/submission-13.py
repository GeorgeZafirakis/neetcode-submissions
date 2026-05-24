class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        if nums == []:
            return [[]]

        res = []
        def dfs(i,subSet,curSum):

            # Base Case
            if i >= len(nums) or curSum > target:
                return

            if curSum == target:
                res.append(subSet.copy())
                return 

            # Recursive Case
            subSet.append(nums[i])
            dfs(i, subSet, curSum + nums[i])
            subSet.remove(nums[i])
            dfs(i+1, subSet, curSum)
            return


        dfs(0,[],0)
        return res