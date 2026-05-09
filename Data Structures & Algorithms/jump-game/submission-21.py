class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        q = deque([0])
        visited = set([0])
        farthest = 0

        while q:

            i = q.popleft()
            if i == n - 1:
                return True

            start = max(farthest + 1, i + 1)
            end = min(i + nums[i], n - 1)

            for j in range(start, end + 1):

                if j not in visited:
                    q.append(j)
                    visited.add(j)

            farthest = max(farthest, end)

        return False

            