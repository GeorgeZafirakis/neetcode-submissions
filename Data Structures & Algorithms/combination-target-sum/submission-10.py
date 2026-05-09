class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
                 
        nums.sort()
        res = []

        def dfs(i, curSum, curList):

            # Base Case
            if curSum == target:
                res.append(curList.copy())
                return

            # Recursive Case
            for j in range(i, len(nums)):
                
                if curSum + nums[j] > target:
                    return

                curList.append(nums[j])
                dfs(j, curSum + nums[j], curList)
                curList.pop()

        dfs(0,0,[])
        return res

                
