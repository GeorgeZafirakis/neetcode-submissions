class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [ [] for i in range(n) ]
        visited = set()

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):

            # Base Case
            if node in visited:
                return 
            
            # Recursive Case
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            return

        res = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        return res

        