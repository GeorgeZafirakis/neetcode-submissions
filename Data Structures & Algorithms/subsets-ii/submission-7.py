class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res  = []
        seen = set()
        nums.sort()

        def dfs(i, curList):

            # Base Case
            if i >= len(nums) and tuple(curList.copy()) not in seen:
                res.append(curList.copy())
                seen.add(tuple(curList.copy()))
                return

            if i >= len(nums) or tuple(curList.copy()) in seen:
                return

            # Recursive Case
            curList.append(nums[i])
            dfs(i+1,curList)
            curList.pop()
            dfs(i+1,curList)

        dfs(0,[])
        return res