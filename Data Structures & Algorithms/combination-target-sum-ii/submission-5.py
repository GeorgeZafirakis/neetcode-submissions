class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.res = []
        candidates.sort()

        def dfs(i, subset, total):

            # Base Case
            if total == target:
                self.res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # Recursive Case
            subset.append(candidates[i])
            total += candidates[i]
            dfs(i+1, subset, total)
            subset.pop()
            total -= candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, subset, total)

        dfs(0, [], 0)
        return self.res



