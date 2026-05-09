class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, curList, curSum):

            # Base Case
            if curSum == target:
                res.append(curList.copy())
                return

            if i >= len(nums) or sum(curList) > target:
                return

            # Recursive Case
            curList.append(nums[i])
            curSum += nums[i]
            dfs(i, curList, curSum)
            curList.pop()
            curSum -= nums[i]
            dfs(i+1, curList, curSum)

        dfs(0,[], 0)
        return res