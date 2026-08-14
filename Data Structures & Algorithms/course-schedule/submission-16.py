class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = { i : [] for i in range(numCourses) }
        visited   = set()
        completed = set()

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def dfs(crs):

            # Base Case
            if crs in visited:
                return False

            if adj[crs] == [] or crs in completed:
                return True

            # Recursive Case
            visited.add(crs)

            for pre in adj[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            completed.add(crs)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True