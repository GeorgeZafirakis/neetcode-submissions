class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k
        buckets = [0] * k

        nums.sort(reverse=True)

        def dfs(i):

            # All numbers placed
            if i == len(nums):
                return True

            for j in range(k):

                # Try placing nums[i]
                if buckets[j] + nums[i] <= target:

                    buckets[j] += nums[i]

                    if dfs(i + 1):
                        return True

                    buckets[j] -= nums[i]

                # Optimization
                if buckets[j] == 0:
                    break

            return False

        return dfs(0)