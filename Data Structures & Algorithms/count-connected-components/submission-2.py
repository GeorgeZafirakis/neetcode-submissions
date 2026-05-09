class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for i in range(n)]
        visited = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):

            # Base Case
            if visited[node] == True:
                return

            # Recursive Case
            visited[node] = True
            for nei in adj[node]:
                dfs(nei)

        res = 0
        for node in range(n):
            if not visited[node]:
                dfs(node)
                res += 1
        return res