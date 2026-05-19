class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()

        # Create adjacency matrix
        preMap = { i : [] for i in range(numCourses) }
        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(c):

            # Base Case
            if c in visited:
                return False

            if not preMap[c]:
                return True

            # Recursive Case
            visited.add(c)

            for pre in preMap[c]:
                if not dfs(pre):
                    return False
            visited.remove(c)
            return True  

        for crs, pre in prerequisites:
            if not dfs(crs):
                return False
        return True



        