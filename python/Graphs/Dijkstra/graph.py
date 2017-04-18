import sys
from heap import *

class GraphEdge:
    targetNode = None
    weight = None
    def __init__(self, targetNode, weight):
        self.targetNode = targetNode
        self.weight = weight

class GraphNode:
    nodeNum = 0
    neighbours = None
    def __init__(self, nodeNum):
        self.nodeNum = nodeNum
        self.neighbours = []
    def addNeighbour(self, node, distance):
        self.neighbours.append(GraphEdge(node, distance))

class Graph:
    N = 0
    nodes = None
    def __init__(self, N):
        self.nodes = [None]
        self.N = N
        for i in range(N): self.nodes.append(GraphNode(i+1))

    def loadFromInput(self):
        print("loading from file")
        line1 = sys.stdin.readline().split()
        n = int(line1[0]); m=int(line1[1])
        print("n=", n, "m=", m)
        self.__init__(n)
        for i in range(m):
            line = sys.stdin.readline().split()
            n1 = int(line[0]); n2 = int(line[1]); dist = int(line[2])
            self.nodes[n1].addNeighbour(n2, dist)
            self.nodes[n2].addNeighbour(n1, dist)

    def findShortestPath(self, startNode, endNode):
        # prepare structures:
        heap = Heap(self.N)
        prev = [0] * (self.N+1)
        dist = [-1] * (self.N+1)
        heapNodes = [None] * (self.N+1)
        handled = [False] * (self.N+1)
        # initialize:
        prev[startNode] = None
        dist[startNode] = 0
        handled[startNode] = True
        for edge in self.nodes[startNode].neighbours:
            neighbour = edge.targetNode
            distance = edge.weight
            heapNodes[neighbour] = heap.insert(neighbour, distance)
            dist[neighbour] = edge.weight
            prev[neighbour] = startNode
        # main loop
        while heap.size>0:
            (node, distance) = heap.removeMin()
            #print("!", node, distance)
            dist[node] = distance
            handled[node] = True
            for edge in self.nodes[node].neighbours:
                neighbour = edge.targetNode
                if handled[neighbour]: continue
                distance = dist[node] + edge.weight
                if dist[neighbour]==-1:
                    # first-timer:
                    dist[neighbour] = distance
                    prev[neighbour] = node
                    heapNodes[neighbour] = heap.insert(neighbour, distance)
                else:
                    if distance < dist[neighbour]:
                        # we have shorter distance, so update structures:
                        dist[neighbour] = distance
                        prev[neighbour] = node
                        heap.decreaseValue(heapNodes[neighbour], distance)
            if node == endNode:
                break
        if dist[endNode] == -1: print("No route found :(")
        else:
            node = endNode
            route=[node]
            while prev[node] != None:
                node = prev[node]
                route.append(node)
            route.reverse()
            for node in route: print("Node:", node)
        print("Total distance:", dist[endNode])
        return dist[endNode]

    def printSelf(self):
        print("Graph with n=", self.N)
        for i in range(self.N):
            node = i+1
            print("Node ", node)
            for edge in self.nodes[node].neighbours:
                print("  ->", edge.targetNode, edge.weight)

#TESTING

g = Graph(0)
g.loadFromInput()
g.findShortestPath(8, 5)

