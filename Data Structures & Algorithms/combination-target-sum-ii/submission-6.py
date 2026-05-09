class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def dfs(i, curList, curSum):

            # Base Case
            if curSum == target:
                res.append(curList.copy())
                return

            if i >= len(candidates) or curSum > target:
                return

            # Recursive Case
            curList.append(candidates[i])
            curSum += candidates[i]
            dfs(i+1, curList, curSum)
            curList.pop()
            curSum -= candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1 
            dfs(i+1, curList, curSum)

        dfs(0,[], 0)
        return res