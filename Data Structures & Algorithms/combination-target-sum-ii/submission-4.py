class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        
        def dfs(i, subset):

            # Base Case
            total = sum(subset)
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >= len(candidates):
                return

            # Recursive Case
            subset.append(candidates[i])
            dfs(i+1, subset)
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, subset)


        dfs(0, [])
        return res



