import random


class CountSort:

    def __init__(self, minValue, maxValue):
        self.minValue = minValue
        self.maxValue = maxValue

    def randomTable(numberOfObjects, minValue, maxValue):
        table = []
        random.seed()  # initialize random generator, where current time is seed parameter
        for i in range(numberOfObjects):
            table.append(
                random.randint(minValue, maxValue))  # add into the table int number, where minValue<= number <=maxValue
        return table

    def sort(self, numberOfObjects, tableToSort):
        temporaryList = [0] * self.maxValue  # 10000 is the maximum value
        for number in tableToSort:
            temporaryList[number - 1] += 1  # count each object in 'tableToSort'
        sortIndex = 0
        for i in range(self.maxValue):
            for j in range(temporaryList[i]):
                tableToSort[sortIndex] = i + 1
                sortIndex += 1
        return tableToSort

    def sortRandom(self, numberOfObjects):
        tableToSort = CountSort.randomTable(numberOfObjects, self.minValue, self.maxValue)
        temporaryList = [0] * self.maxValue  # 10000 is the maximum value
        for number in tableToSort:
            temporaryList[number - 1] += 1  # count each object in 'tableToSort'
        sortIndex = 0
        for i in range(self.maxValue):
            for j in range(temporaryList[i]):
                tableToSort[sortIndex] = i + 1
                sortIndex += 1
        return tableToSort

    
    def sortStable(self, numberOfObjects):
        tableToSort = CountSort.randomTable(numberOfObjects, self.minValue, self.maxValue)
        sortedTable = [0] * numberOfObjects
        temporaryList = [0] * (self.maxValue+1)  # 10000 is the maximum value
        for number in tableToSort:
            temporaryList[number] += 1  # count each object in 'tableToSort'
        for i in range(1, self.maxValue+1):     # Count position for particular index from temporaryList in final tableToSort, temporaryList[0] is already ok
            temporaryList[i] = temporaryList[i-1]+temporaryList[i]
        i = numberOfObjects - 1
        while i>=0:
            print(i, tableToSort[i])
            sortedTable[temporaryList[tableToSort[i]]-1]=tableToSort[i]
            temporaryList[tableToSort[i]] -= 1
            i -= 1

        return sortedTable

print("Start")
x = CountSort(1, 10000)
print(x.sort(8, [7, 20, 3, 4, 7, 15, 10, 8]))
print(x.sortRandom(100000))
print(x.sortStable(100000))
