class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        q = deque([0])

        while q:

            i = q.popleft()
            if i == n - 1:
                return True

            for j in range(i+1, min(i + nums[i] + 1)):
                q.append(j)

        return False



class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        q = deque([0])          # store indices
        visited = set([0])      # avoid revisiting

        while q:
            i = q.popleft()

            if i == n - 1:
                return True

            # explore all reachable positions
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                if j not in visited:
                    visited.add(j)
                    q.append(j)

        return False
            