import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #다익스트라 특정 노드에 특정 노드까지 최단 거리를 찾는 문제
        INF = int(1e9)
        distances = [INF] * (n + 1)
        graph = [[] for _ in range(n + 1)]
        for start, end, cost in times:
            graph[start].append((cost, end))

        def dijkstra(startNode):
            queue = []
            distances[startNode] = 0
            heapq.heappush(queue, (startNode, distances[startNode]))

            while queue:
                cur, curCost = heapq.heappop(queue)

                if distances[cur] < curCost:
                    continue
                
                for i in graph[cur]:
                    newCost = curCost + i[0]
                    if newCost < distances[i[1]]:
                        distances[i[1]] = newCost
                        heapq.heappush(queue, (i[1], newCost))
        
        dijkstra(k)
        distances[0] = 0
        # 전부 도달 하지 못한 경우
        if max(distances) == INF:
            return -1
        else:
            return max(distances)


        