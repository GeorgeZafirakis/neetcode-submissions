class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(candidates)
        res = []

        def dfs(i, curSum, curList):

            # Base Case
            if curSum == target:
                res.append(curList.copy())
                return

            if i >= len(nums) or curSum > target:
                return

            # Recursive Case
            curList.append(nums[i])
            curSum += nums[i]
            dfs(i+1,curSum,curList)
            curList.pop()
            curSum -= nums[i]
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1,curSum,curList)

        dfs(0,0,[])
        return res