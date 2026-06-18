# 332. Reconstruct Itinerary

from typing import List
from collections import defaultdict


# Backtracking + Greedy (times out, but is one accepted-style
# solution, keep it for the idea)
# Time: O(e^d)
# Space: O(v+e)
# 2023.10.31: no
# notes: plain backtrack; since the result must be the smallest
#        lexical order, sort each destination list before backtracking
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        self.visitBitmap = {}

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort()
            self.visitBitmap[origin] = [False]*len(itinerary)

        self.flights = len(tickets)
        self.result = []
        route = ['JFK']
        self.backtracking('JFK', route)

        return self.result

    def backtracking(self, origin, route):
        if len(route) == self.flights + 1:
            self.result = route
            return True

        for i, nextDest in enumerate(self.flightMap[origin]):
            if not self.visitBitmap[origin][i]:
                # mark the visit before the next recursion
                self.visitBitmap[origin][i] = True
                ret = self.backtracking(nextDest, route + [nextDest])
                self.visitBitmap[origin][i] = False
                if ret:
                    return True

        return False


# Hierholzer's Algorithm
# Time: O(elog(e/v))
# Space: O(v+e)
# 2023.10.31: no
# notes: clever, see the editorial:
# https://leetcode.com/problems/reconstruct-itinerary/editorial/
# build the map, sort each list in reverse, then DFS; when a node
# is a dead end append it to the result, the DFS runs in reverse
# so reverse the result at the end with [::-1]
class Solution2:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)

        self.result = []
        self.DFS('JFK')

        # reconstruct the route backwards
        return self.result[::-1]

    def DFS(self, origin):
        destList = self.flightMap[origin]
        while destList:
            #while we visit the edge, we trim it off from graph.
            nextDest = destList.pop()
            self.DFS(nextDest)
        self.result.append(origin)


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.findItinerary(
        [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"],
         ["ATL", "JFK"], ["ATL", "SFO"]]
    ) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    assert sol.findItinerary(
        [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    ) == ["JFK", "MUC", "LHR", "SFO", "SJC"]
