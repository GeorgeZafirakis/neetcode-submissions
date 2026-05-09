class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        q = deque([(0,0)]) # (index,steps)
        visited = set([0])
        res = 0

        while q:

            i, s = q.popleft()
            if i == n - 1:
                return s

            for j in range(i, min(i + nums[i] + 1, n)):

                if j not in visited:
                    q.append((j,s+1))
                    visited.add(j)

        return -1

