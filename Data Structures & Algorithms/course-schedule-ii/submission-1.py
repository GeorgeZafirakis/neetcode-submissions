class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        path = set()
        safe = set()
        order = []

        def dfs(node):
            if node in path:
                return False
            if node in safe:
                return True

            path.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            path.remove(node)
            safe.add(node)
            order.append(node)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return []
        return order
