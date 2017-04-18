import sys
from heap import *
import math

class GraphEdge:
    targetNode = None
    weight = None
    def __init__(self, targetNode, weight):
        self.targetNode = targetNode
        self.weight = weight

class GraphNode:
    nodeNum = 0
    x = None;
    y = None;

    neighbours = None
    def __init__(self, nodeNum, x, y):
        self.nodeNum = nodeNum
        self.x = x
        self.y = y
        self.neighbours = []
    def addNeighbour(self, node, distance):
        self.neighbours.append(GraphEdge(node, distance))

class Graph:
    N = 0
    nodes = None
    def __init__(self, N):
        self.nodes = [None]
        self.N = N
        for i in range(N): self.nodes.append(GraphNode(i+1, 0 , 0))

    def loadFromInput(self):
        print("loading from file")
        line1 = sys.stdin.readline()
        n = int(line1);
        print("n=", n)
        self.__init__(n)
        for i in range(n):
            line = sys.stdin.readline().split()
            x = int(line[0]); y = int(line[1]);
            self.nodes[i + 1].x = x
            self.nodes[i + 1].y = y
            m = int(line[2]);
            for j in range(m):
                neighbour = int(line[3 + j])
                self.nodes[i+1].addNeighbour(neighbour, 0) # we do not know yet the distance
        for i in range (n):
            for edge in self.nodes[i+1].neighbours:
                edge.weight = self.calculateDistance(self.nodes[i+1].nodeNum, edge.targetNode)
                print("start node: "+  str(self.nodes[i+1].nodeNum) + " end node: " + str(edge.targetNode) +  " distance: " + str(edge.weight))

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
                ax = self.nodes[node].x - self.nodes[prev[node]].x
                ay = self.nodes[node].y - self.nodes[prev[node]].y
                bx = self.nodes[neighbour].x - self.nodes[node].x
                by = self.nodes[neighbour].y - self.nodes[node].y
                if Graph.goesLeft(ax, ay, bx, by): continue
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

    @staticmethod
    # returns True if vector b (bx, by, 0) lies to the left of vector a(ax, ay, 0)
    # c (cx, cy, cz) = a x b - if  ay, by == 0 then cx, cy i always 0
    def goesLeft(ax, ay, bx, by):
        cz = ax * by - ay * bx
        if cz > 0:
            return True
        else:
            return False

    # calculates distance between two nodes
    def calculateDistance(self, startNode, endNode):
        dist = math.sqrt(math.pow((self.nodes[endNode].x - self.nodes[startNode].x), 2) + math.pow((self.nodes[endNode].y - self.nodes[startNode].y), 2))
        return dist

    def printSelf(self):
        print("Graph with n=", self.N)
        for i in range(self.N):
            node = i+1
            print("Node ", node)
            for edge in self.nodes[node].neighbours:
                print("  ->", edge.targetNode, edge.weight)

g = Graph(0)
g.loadFromInput()
g.findShortestPath(1, 7)



