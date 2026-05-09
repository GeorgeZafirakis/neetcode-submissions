class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > n - 1:
            return False

        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node, par):

            # Base Case
            if node in visited:
                return False

            # Recursive Case
            
            visited.add(node)
            # For all neighbours of current node
            for nei in adj[node]:
                # If we reach current node from parrent, then skip
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)




