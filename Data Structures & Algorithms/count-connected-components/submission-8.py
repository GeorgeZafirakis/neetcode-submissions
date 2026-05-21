class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        visited = set()
        preMap = { i : [] for i in range(n) }
        for u,v in edges:
            preMap[u].append(v)
            preMap[v].append(u)

        def dfs(node):

            # Base Case
            if node in visited:
                return 

            # Recursive Case
            visited.add(node)
            for nei in preMap[node]:
                dfs(nei)


        res = 0
        for node in range(n):
            if not node in visited:
                dfs(node)
                res += 1
        return res