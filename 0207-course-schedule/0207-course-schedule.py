from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        result = False
        # 싸이클이 존재하면 False
        graph = [[] for _ in range(numCourses)]
        for i,j in prerequisites:
            graph[j].append(i)

        visited = [0] * numCourses

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1
            for i in graph[node]:
                if not dfs(i):
                    return False
            visited[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
        