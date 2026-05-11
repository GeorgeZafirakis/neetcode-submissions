class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
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
            dfs(i,subSet,curSum + nums[i])
            subSet.pop()
            dfs(i+1,subSet,curSum)
            return


        dfs(0,[],0)
        return res


