class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res = []

        def dfs(i, curSum, curList):

            # Base Case
            if i >= len(nums) or curSum > target:
                return

            if curSum == target:
                res.append(curList.copy())
                return

            # Recursive Case
            curList.append(nums[i])
            curSum += nums[i]
            dfs(i,curSum,curList)
            curList.pop()
            curSum -= nums[i]
            dfs(i+1,curSum,curList)

        dfs(0,0,[])
        return res