class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()
        preMap = { i : [] for i in range(numCourses) }

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):

            # Base Case
            if crs in visited:
                return False

            if crs == []:
                return True

            # Recursive Case
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True