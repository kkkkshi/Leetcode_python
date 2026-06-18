# 743. Network Delay Time

import heapq
from collections import defaultdict, deque
from queue import PriorityQueue


# Dijkstra Approach (best approach)
# Time: O(n + elogn)
# Space: O(n + e)
# 2023.07.10: yes
# notes: Dijkstra from k with a priority queue; answer is the max of
#        all shortest distances, or -1 if any node is unreachable
class Solution:
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = [[] for _ in range(n+1)]
        for edge in times:
            from_node, to_node, weight = edge[0], edge[1], edge[2]
            graph[from_node].append([weight, to_node])

        def dijkstra(start, graph):
            distTo = [float('inf')] * (n+1)
            distTo[start] = 0
            pq = PriorityQueue()
            pq.put([0, start])

            while not pq.empty():
                curState = pq.get()
                curNodeID, curDistFromStart = curState[1], curState[0]

                if curDistFromStart > distTo[curNodeID]:
                    continue
                for nextNode in graph[curNodeID]:
                    nextNodeID, nextNodeWeight = nextNode[1], nextNode[0]
                    distToNextNode = distTo[curNodeID] + nextNodeWeight
                    if distTo[nextNodeID] > distToNextNode:
                        distTo[nextNodeID] = distToNextNode
                        pq.put([distToNextNode, nextNodeID])
            return distTo
        distTo = dijkstra(k, graph)
        res = 0
        for dist in distTo[1:]:
            if dist == float('inf'):
                return -1
            res = max(res, dist)
        return res


# Dijkstra Approach (best approach)
# Time: O((n-1)!+eloge)
# Space: O(n + e)
# 2023.07.10: yes
# notes: someone else's optimized version, slick
class Solution2:
    def networkDelayTime(self, times, N, K):
        elapsedTime, graph, heap = [0] + [float("inf")] * N, defaultdict(list), [(0, K)] # it's a min-heap
        for u, v, w in times:
            graph[u].append((v, w))
        while heap:
            time, node = heapq.heappop(heap)
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    heapq.heappush(heap, (time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1


# Depth-First Search Approach
# Time: O(n + elogn)
# Space: O(n + e)
# 2023.07.10: no
# notes: DFS relaxing distances, visiting neighbours in sorted order
#        and pruning when the current path is not shorter
class Solution3:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        distance = {node: float("inf") for node in range(1, N + 1)}
        self.DFS(graph, distance, K, 0)
        totalTime = max(distance.values())
        return totalTime if totalTime < float("inf") else -1

    def DFS(self, graph, distance, node, elapsedTimeSoFar):
        if elapsedTimeSoFar >= distance[node]:   # signal aalreaady reached to this node. so no need to explore for this node
            return
        distance[node] = elapsedTimeSoFar
        for neighbour, time in sorted(graph[node]):
            self.DFS(graph, distance, neighbour, elapsedTimeSoFar + time)


# Breadth-First Search Approach
# Time: O(ne)
# Space: O(ne)
# 2023.07.10: no
# notes: BFS over a queue, relaxing each node's distance and
#        re-enqueueing neighbours whenever a shorter time is found
class Solution4:
    def networkDelayTime(self, times, N, K):
        elapsedTime, graph, queue = [0] + [float("inf")] * N, defaultdict(list), deque([(0, K)])
        for u, v, w in times:
            graph[u].append((v, w))
        while queue:
            time, node = queue.popleft()
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    queue.append((time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1


# below are other people's algorithms, worth revisiting later
# Original Bellman-Ford algorithm - Accepted
# Time: O(ne)
# Space: O(n)
# notes: relax every edge N-1 times; works with 0-based indexing on
#        the distance array
class Solution5:
    def networkDelayTime(self, times, N, K):
        distance = [float("inf") for _ in range(N)]
        distance[K-1] = 0
        for _ in range(N-1):
            for u, v, w in times:
                if distance[u-1] + w < distance[v-1]:
                    distance[v-1] = distance[u-1] + w
        return max(distance) if max(distance) < float("inf") else -1


# Shortest Path Faster Algorithm (SPFA): An improvement of the Bellman-Ford algorithm - Accepted
# Time: O(ne)
# Space: O(n + e)
# notes: queue-based Bellman-Ford; only re-process a node when its
#        distance improves
class Solution6:
    def networkDelayTime(self, times, N, K):
        elapsedTime, graph, queue = [0] + [float("inf")] * N, defaultdict(list), deque([(0, K)])
        elapsedTime[K] = 0
        for u, v, w in times:
            graph[u].append((v, w))
        while queue:
            time, node = queue.popleft()
            for neighbour in graph[node]:
                v, w = neighbour
                if time + w < elapsedTime[v]:
                    elapsedTime[v] = time + w
                    queue.append((time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1


# Floyd Warshall - Accepted
# Time: O(n^3)
# Space: O(n^2)
# notes: all-pairs shortest paths; answer is the max over row K-1
class Solution7:
    def networkDelayTime(self, times, N, K):
        elapsedTimeMatrix = [[float("inf") for _ in range(N)] for _ in range(N)]
        for u, v, w in times:
            elapsedTimeMatrix[u - 1][v - 1] = w
        for i in range(N):                      #   Assigning 0 to the diagonal cells
            elapsedTimeMatrix[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    elapsedTimeMatrix[i][j] = min(elapsedTimeMatrix[i][j], elapsedTimeMatrix[i][k] + elapsedTimeMatrix[k][j])
        mx = max(elapsedTimeMatrix[K - 1])
        return mx if mx < float("inf") else -1


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4(),
            Solution5(), Solution6(), Solution7()):
    assert sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert sol.networkDelayTime([[1, 2, 1]], 2, 1) == 1
    assert sol.networkDelayTime([[1, 2, 1]], 2, 2) == -1
