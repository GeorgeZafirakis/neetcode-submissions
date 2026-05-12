class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        # Base Case
        if nums == []:
            return [[]]

        # Recursive Case
        perms = self.permuteUnique(nums[1:])
        for p in perms:
            n = len(p)
            for i in range(n+1):
                p_copy = p.copy()
                p_copy.insert(i,nums[0])
                res.append(p_copy)

        mySet = set()
        for r in res:
            mySet.add(tuple(r))

        return [list(x) for x in mySet]