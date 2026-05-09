class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]  # start with the empty subset

        for num in nums:
            # for each existing subset, create a new one including num
            new_subsets = []
            for subset in res:
                new_subsets.append(subset + [num])

            # add the new subsets to the result
            res = res + new_subsets

        return res
        