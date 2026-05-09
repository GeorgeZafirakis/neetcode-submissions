class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()     # recursion stack
        processed = set()   # fully processed nodes
        order = []
        
        def dfs(crs):

            # cycle detected
            if crs in visited:
                return False

            # already processed
            if crs in processed:
                return True

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            processed.add(crs)
            order.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return order