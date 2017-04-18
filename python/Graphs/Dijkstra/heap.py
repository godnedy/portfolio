class HeapNode:
    index = 0
    object = None
    value = None
    def __init__(self, index, object, value):
        self.index = index
        self.object = object
        self.value = value

class Heap:
    size = 0
    arr = None
    def __init__(self, maxSize):
        self.size = 0
        self.arr = [None] * (maxSize+1)

    # inserts new element into heap
    # returns heapNode, which could be later used in decreaseValue()
    def insert(self, something, value):
        self.size += 1
        newNode = HeapNode(self.size, something, value)
        self.arr[self.size]= newNode
        self.__upHeap(self.size)
        return newNode

    # removes element with smallest value
    # returns anObject, aValue
    def removeMin(self):
        minObject = self.arr[1].object
        minValue = self.arr[1].value
        self.__swap(1, self.size)
        self.size -= 1
        self.__downHeap()
        return minObject, minValue

    # decreases value for given node
    # Assumption: newValue is less or equal previous value (it really is decreasing)
    def decreaseValue(self, heapNode, newValue):
        heapNode.value = newValue
        self.__upHeap(heapNode.index)

    # private
    def __downHeap(self):
        index = 1
        while index < self.size:
            newIndex = self.__downHeapNode(index)
            if newIndex == index:
                return
            else:
                index = newIndex

    def __downHeapNode(self, index):
        child1 = index*2
        child2 = index*2+1
        swap = index
        if child1 <= self.size:
            if self.arr[child1].value < self.arr[swap].value: swap = child1
        if child2 <= self.size:
            if self.arr[child2].value < self.arr[swap].value: swap = child2
        if swap != index: self.__swap(index, swap)
        return swap

    def __upHeapNode(self, index):
        # assumption: index>1, so it is not a root node
        parent = int(index / 2)
        #print("upheadnode index=", index, "parent=", parent)
        if self.arr[parent].value > self.arr[index].value:
            #print("swapping")
            self.__swap(index, parent)
            return parent
        else:
            return index

    def __upHeap(self, startIndex):
        index = startIndex
        while index>1:
            newIndex = self.__upHeapNode(index)
            if newIndex == index: return
            else: index = newIndex

    def __swap(self, index1, index2):
        node1 = self.arr[index1]
        node2 = self.arr[index2]
        node1.index = index2; self.arr[index2] = node1
        node2.index = index1; self.arr[index1] = node2

    # checks if heap is correct
    def checkHeap(self):
        for i in range(self.size):
            index = i+1
            child1 = index*2
            child2 = index*2+1
            if (child1 <= self.size and self.arr[child1].value<self.arr[index].value) or \
                (child2 <= self.size and self.arr[child2].value<self.arr[index].value):
                print("Heap is incorrect! Position: ", index)
        print("Correct")

    @staticmethod
    def performTests():
        h = Heap(100)
        nodes = {}
        for v in range(50, 10, -2):
            print("Inserting ", v)
            nodes[v] = h.insert("Testy", v)
            h.checkHeap()

        h.decreaseValue(nodes[40], 19)
        h.checkHeap()
        h.decreaseValue(nodes[12], 10)
        h.checkHeap()
        h.decreaseValue(nodes[50], 36)
        h.checkHeap()

        while h.size>0:
            (obj, value) = h.removeMin()
            print(obj, value)
            h.checkHeap()


#TESTING
Heap.performTests()