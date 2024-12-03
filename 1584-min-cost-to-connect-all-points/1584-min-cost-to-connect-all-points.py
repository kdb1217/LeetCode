import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]
        result = 0

        while len(visited) < n:
            cost, curr = heapq.heappop(min_heap)

            if curr in visited:
                continue

            visited.add(curr)
            result += cost

            for i in range(n):
                if i not in visited:
                    dist = self.getDistance(points[curr], points[i])
                    heapq.heappush(min_heap, (dist, i))
        return result
    

    # 거리구하는 함수
    def getDistance(self, dot1, dot2):
        i1, j1 = dot1[0], dot1[1]
        i2, j2 = dot2[0], dot2[1]
        return abs(i1 - i2) + abs(j1 - j2)