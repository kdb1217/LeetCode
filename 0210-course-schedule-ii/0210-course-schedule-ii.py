from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 위상 정렬 알고리즘 사용해서 하기
        adj_list = [[] for _ in range(numCourses)] #그래프로 만들기
        in_degree = [0] * numCourses # 차수
        result = []

        for i, j in prerequisites:
            adj_list[j].append(i)
            in_degree[i] += 1

        queue = deque()

        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)

        visited_count = 0

        while queue:
            node = queue.popleft()
            visited_count += 1

            for i in adj_list[node]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
            
            result.append(node)

        if len(result) == numCourses:
            return result
        else:
            return []



        