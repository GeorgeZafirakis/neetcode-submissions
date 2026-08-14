class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visiting = set()
        completed = set()

        def dfs(crs):

            # Cycle detected
            if crs in visiting:
                return False

            # Already completely checked
            if crs in completed:
                return True

            visiting.add(crs)

            for pre in adj[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            completed.add(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True