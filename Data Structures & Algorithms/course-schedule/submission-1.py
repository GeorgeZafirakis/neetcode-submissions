class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()

        def dfs(crs):

            # Base Case
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True

            # Recursive Case
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                    
            visit.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True