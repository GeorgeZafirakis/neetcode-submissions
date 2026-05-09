class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.res = []

        def dfs(i, subset, total):

            # Base Case
            if i >= len(nums) or total > target:
                return
            if total == target:
                self.res.append(subset.copy())
                return

            # Recursive Case
            subset.append(nums[i])
            total += nums[i]
            dfs(i, subset, total)
            subset.pop()
            total -= nums[i]
            dfs(i+1, subset, total)

        dfs(0, [], 0)
        return self.res