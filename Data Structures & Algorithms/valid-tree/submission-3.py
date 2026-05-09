class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        preMap = {i : [] for i in range(n)}
        for u, v in edges:
            preMap[u].append(v)
            preMap[v].append(u)

        visited = set()

        def dfs(node, prev):

            # Base Case
            if node in visited:
                return False

            # Recursive Case
            visited.add(node)
            for nei in preMap[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0,-1) and len(visited) == n