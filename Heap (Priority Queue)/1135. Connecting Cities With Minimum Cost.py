# 1135. Connecting Cities With Minimum Cost

# Minimum Spanning Tree (Using Kruskal's algorithm) Approach
# Time: O(mlogm) for sorting
# Space: O(n)
# 2023.07.06: yes
# notes: sort edges by cost, union endpoints if not already joined,
#        add the cost; connected iff exactly one component remains
class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.size = [1] * n
        self.count = n-1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ

    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)
        if root_A == root_B:
            return
        if self.size[root_A] < self.size[root_B]:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
        else:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
        self.count -= 1


class Solution:
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        mst = 0
        ufs = UnionFind(n+1)
        sorted_connections = sorted(connections, key=lambda x: x[2])
        for connection in sorted_connections:
            if ufs.connected(connection[0], connection[1]):
                continue
            else:
                ufs.union(connection[0], connection[1])
                mst += connection[2]
        return mst if ufs.count==1 else -1


# Prim Approach
# Time: O(eloge)
# Space: O(e+v)
# 2023.07.06: yes
# notes: grow the tree from node 0, keep crossing edges in a heap,
#        always pull the cheapest edge to an outside node
import heapq
class Prim:
    # core structure: a priority queue holding the crossing edges
    def __init__(self, graph):
        self.graph = graph
        self.pq = []  # the PriorityQueue<int[]> implementation
        self.inMST = [False] * len(graph)  # like visited: nodes already in the MST
        self.weightSum = 0  # total weight of the MST
        self.inMST[0]= True  # start from any node; node 0 here
        self.cut(0)
        # keep cutting, adding edges to the MST
        while self.pq:
            # ordered by edge weight, smallest first
            edge = heapq.heappop(self.pq)
            to = edge[2]  # the adjacent node
            weight = edge[0]  # this edge's weight
            if self.inMST[to]:  # node to already in MST, skip; else it makes a cycle
                continue
            self.weightSum += weight  # add edge to the MST
            self.inMST[to] = True
            self.cut(to)  # node to joined, cut again for more crossing edges

    # add the crossing edges of s into the priority queue
    def cut(self, s):
        for edge in self.graph[s]:  # walk s's neighbors
            to = edge[2]  # the adjacent node
            if self.inMST[to]:  # neighbor to already in MST, skip
                continue
            heapq.heappush(self.pq, edge)  # push the crossing edge

    # total weight of the MST
    def weight(self):
        return self.weightSum

    # whether the MST covers every node in the graph
    def allConnected(self) -> bool:
        for i in range(len(self.inMST)):
            if not self.inMST[i]:
                return False
        return True


class Solution2:
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for connection in connections:
            u = connection[0]-1
            v = connection[1]-1
            graph[u].append([connection[2],u,v])
            graph[v].append([connection[2],v,u])
        prim = Prim(graph)
        if not prim.allConnected():
            return -1
        return prim.weight()


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.minimumCost(3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]) == 6
    assert sol.minimumCost(4, [[1, 2, 3], [3, 4, 4]]) == -1
    assert sol.minimumCost(2, [[1, 2, 7]]) == 7
