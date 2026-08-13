class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        nums = sorted(candidates)

        def dfs(i, curList, curSum):

            if curSum == target:
                res.append(curList.copy())
                return

            if i >= len(nums) or curSum > target:
                return

            curList.append(nums[i])
            dfs(i+1, curList, curSum + nums[i])
            curList.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, curList, curSum)
            return

        dfs(0, [], 0)
        return res
