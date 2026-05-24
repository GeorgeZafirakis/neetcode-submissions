class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(candidates)

        if nums == []:
            return [[]]

        res = []
        def dfs(i,subSet,curSum):

            # Base Case
            if curSum == target:
                res.append(subSet.copy())
                return 

            if i >= len(nums) or curSum > target:
                return

            # Recursive Case
            subSet.append(nums[i])
            dfs(i+1, subSet, curSum + nums[i])
            subSet.pop()
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, subSet, curSum)


        dfs(0,[],0)
        return res