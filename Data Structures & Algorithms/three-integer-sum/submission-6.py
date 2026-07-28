class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Optimization: no possible triplets beyond this
            if nums[i] > 0:
                break

            l, r = i + 1, n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicates for l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res