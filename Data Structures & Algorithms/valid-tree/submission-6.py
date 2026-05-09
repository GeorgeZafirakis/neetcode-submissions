class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n != len(edges) + 1:
            return False

        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(node, par):

            # Base Case
            if node in visit:
                return False

            # Recursive Case
            visit.add(node)
            for nei in adj[node]:

                if nei == par:
                    continue

                if nei not in visit:
                    dfs(nei,node)

            return True

        return dfs(0,-1) and len(visit) == n