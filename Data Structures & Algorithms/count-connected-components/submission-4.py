class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for i in range(n)]
        visit = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):

            # Base Case
            if visit[node]:
                return

            # Recursive Case
            visit[node] = True
            for nei in adj[node]:
                dfs(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                dfs(node)
                res += 1
        return res