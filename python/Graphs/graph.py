import sys
from heap import *



class GraphEdge:
    targetNode = None
    weight = None

    def __init__(self, targetNode, weight):
        self.targetNode = targetNode
        self.weight = weight


class GraphNode:
    nodeNum = None
    neighbours = None

    def __init__(self, nodeNum):
        self.nodeNum = nodeNum
        self.neighbours = []

    def addNeighbour(self, node, distance):
        self.neighbours.append(GraphEdge(node, distance))


class Graph:
    N = 0  # number of cities
    K = 0  # number of restaurants

    nodes = None
    restaurants = None
    maxMin = None

    def __init__(self, N, K):
        self.nodes = [None]
        self.restaurants = [None]
        self.N = N
        self.K = K
        for i in range(N): self.nodes.append(GraphNode(i + 1))
        self.maxMin = 0;

    def loadFromInput(self):
        print("loading from file")
        line1 = sys.stdin.readline().split()
        n = int(line1[0])
        k = int(line1[1])
        m = int(line1[2])
        print("n=", n)
        print("k=", k)
        print("m=", m)
        self.__init__(n+1, k) # n+1 because we are creating additional "fake" city
        for i in range(k):  # read restaurants cities and create "fake" edges
            cityNumber = int(sys.stdin.readline())
            self.nodes[self.N].addNeighbour(cityNumber, 0)
            self.nodes[cityNumber].addNeighbour(self.N, 0)
        for i in range(m):
            line = sys.stdin.readline().split()
            n1 = int(line[0]);
            n2 = int(line[1]);
            d = int(line[2])
            self.nodes[n1].addNeighbour(n2, d)
            self.nodes[n2].addNeighbour(n1, d)
            # print("start node: "+  str(self.nodes[i+1].nodeNum) + " end node: " + str(edge.targetNode) +  " distance: " + str(edge.weight))

    def solve(self):  #
        # Dijkstra starting from "fake" node
        self.findShortestPath(self.nodes[int(self.N)].nodeNum)
        return self.maxMin;


    def findShortestPath(self, startNode):
        # prepare structures:
        heap = Heap(self.N)
        prev = [0] * (self.N + 1)
        dist = [-1] * (self.N + 1)
        heapNodes = [None] * (self.N + 1)
        handled = [False] * (self.N + 1)
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
        while heap.size > 0:
            (node, distance) = heap.removeMin()
            if distance > self.maxMin:
                #print("Max min distance increased, curently ", distance)
                self.maxMin = distance
            dist[node] = distance
            handled[node] = True
            for edge in self.nodes[node].neighbours:
                neighbour = edge.targetNode
                if handled[neighbour]: continue
                distance = dist[node] + edge.weight
                if dist[neighbour] == -1:
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

    def printSelf(self):
        print("Graph with n=", self.N)
        for i in range(self.N):
            node = i + 1
            print("Node ", node)
            for edge in self.nodes[node].neighbours:
                print("  ->", edge.targetNode, edge.weight)


g = Graph(0,0)
g.loadFromInput()
print(g.solve())
