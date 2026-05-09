class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
 
#        if len(edges) != n - 1:
#            return False
        
        preMap = {i : [] for i in range(n)}
        for crs, pre in edges:
            preMap[crs].append(pre)
            preMap[pre].append(crs)

        visit = set()
        def dfs(crs, prev):

            # Base Case
            if crs in visit:
                return False

            # Recursive Case
            visit.add(crs)
            for pre in preMap[crs]:
                if pre == prev:
                    continue
                if not dfs(pre, crs):
                    return False           
            return True

        return dfs(0, -1) and len(visit) == n