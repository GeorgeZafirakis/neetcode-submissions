class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        q = deque([0])
        visited = set([0])

        while q:

            i = q.popleft()
            if i == n - 1:
                return True

            for j in range(i+1, min(i + nums[i] + 1, n)):
                q.append(j)
                visited.add(j)

        return False

            