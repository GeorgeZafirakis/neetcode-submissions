class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        nums = [i for i in range(1,n+1)]
        res = []

        def dfs(i,curList):

            # Base Case
            if len(curList) == k:
                res.append(curList.copy())
                return

            if i >= len(nums):
                return

            # Recursive Case
            curList.append(nums[i])
            dfs(i+1,curList)
            curList.pop()
            dfs(i+1,curList)

        dfs(0,[])

        return res
        