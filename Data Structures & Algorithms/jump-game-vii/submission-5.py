class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        q = deque([0])
        visited = set([0])

        while q:

            index = q.popleft()

            for k in range(minJump, maxJump + 1):

                nxt = index + k

                if nxt >= len(s):
                    continue

                if s[nxt] != '0':
                    continue

                if nxt == len(s) - 1:
                    return True

                if s[nxt] == '0' and nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return False