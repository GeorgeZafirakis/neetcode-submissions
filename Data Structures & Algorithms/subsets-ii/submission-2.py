class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        res = set()

        def backtrack(i, subset):
            
            # Base Case
            if i == len(nums):
                res.add(tuple(subset))
                return

            # Recursive Case
            subset.append(nums[i])
            backtrack(i+1, subset)

            subset.pop()
            backtrack(i+1, subset)

        nums.sort()
        backtrack(0, [])
        return [list(s) for s in res]