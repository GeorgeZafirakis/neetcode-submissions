class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        adj = { i : [] for i in range(n) }
        visited = set()
        
        for v,u in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):

            # Base Case
            if node in visited:
                return False

            # Recursive Case
            visited.add(node)
            for nei in adj[node]:

                if nei == parent:
                    continue
                else:
                    dfs(nei,node)

            return True


        return dfs(0,-1) and len(visited) == n