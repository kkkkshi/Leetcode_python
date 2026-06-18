# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

# Array Approach
# Time: O(n^3)
# Space: O(n)
# 2023.07.22: yes
# notes: Floyd-Warshall all-pairs distances, then pick the city
#        with fewest reachable neighbors; not great but works
import collections
import heapq

class Solution:
    def findTheCity(self, n, edges, maxd):
        """
        :type n: int
        :type edges: List[List[int]]
        :type maxd: int
        :rtype: int
        """
        dis = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = {sum(d <= maxd for d in dis[i]): i for i in range(n)}
        return res[min(res)]


# Dijkstra
# Time: O(n^2)
# Space: O(n)
# 2023.07.22: yes
# notes: run Dijkstra from every city, stop expanding past the
#        threshold, then take the city with the fewest reachable
#        neighbors, breaking ties by the larger index
class Solution2:
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        graph = collections.defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def getNumberOfNeighbors(city):
            heap = [(0, city)]
            dist = {}

            while heap:
                currW, u = heapq.heappop(heap)
                if u in dist:
                    continue
                if u != city:
                    dist[u] = currW
                for v, w in graph[u]:
                    if v in dist:
                        continue
                    if currW + w <= distanceThreshold:
                        heapq.heappush(heap, (currW + w, v))
            return len(dist)

        return max([(getNumberOfNeighbors(city), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4) == 3
    assert sol.findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2) == 0
    assert sol.findTheCity(2, [[0,1,10]], 5) == 1
