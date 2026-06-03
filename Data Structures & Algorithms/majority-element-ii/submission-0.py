class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        res = []
        counter = defaultdict()

        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        for it in counter:
            
            if counter[it] > len(nums) // 3:
                res.append(it)

        return res


