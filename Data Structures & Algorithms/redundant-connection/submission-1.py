class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        preMap = { i : [] for i in range(n+1)}

        def dfs(node, prev):

            if node in visited:
                return False

            visited.add(node)
            for nei in preMap[node]:
                if prev == nei:
                    continue
                if not dfs(nei, node):
                    return False
            return True
           
        for u, v in edges:
            
            preMap[u].append(v)
            preMap[v].append(u)
            visited = set()

            if not dfs(u,-1):
                return [u,v]
        return []
        






            