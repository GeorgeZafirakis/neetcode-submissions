class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findMinIndex(nums)

        # Search left part
        res = self.binary_search(nums, 0, pivot - 1, target)
        if res != -1:
            return res

        # Search right part
        return self.binary_search(nums, pivot, len(nums) - 1, target)

    def findMinIndex(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_idx = 0

        while l <= r:
            # If current window is sorted
            if nums[l] <= nums[r]:
                if nums[l] < nums[min_idx]:
                    min_idx = l
                break

            mid = (l + r) // 2
            if nums[mid] < nums[min_idx]:
                min_idx = mid

            # Determine which side to continue searching
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return min_idx

    def binary_search(self, nums: List[int], l: int, r: int, target: int) -> int:
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
