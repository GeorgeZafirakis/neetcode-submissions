class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        preMap = {i : [] for i in range(n)}
        for u, v in edges:
            preMap[u].append(v)
            preMap[v].append(u)
        visited = set()

        def dfs(node, prev):

            # Base Case
            if node in visited:
                return

            # Recursive Case
            visited.add(node)
            for nei in preMap[node]:

                if nei == prev:
                    continue
                
                dfs(nei, node)

        res = 0
        for node in range(n):
            if not node in visited:
                dfs(node,-1)
                res += 1
        return res




