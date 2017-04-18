import random
#NIE DO KONCA DZIALA - do poprawy

random.seed()  # initialize random generator, where current time is seed parameter


def switch (a, b, table):
    temp = table[a]
    table[a] = table[b]
    table[b] = temp

class QuickSort:
    def __init__(self, minValue, maxValue):
        self.minValue = minValue
        self.maxValue = maxValue
        self.table = []


    def divide(self, beginningOfTable, endOfTable, randomValue):
        i = beginningOfTable
        j = endOfTable

        while j-i >= 0:
            while self.table[i] < randomValue:
                i += 1
            while self.table[j] > randomValue:
                j -= 1
            if (j - i) >= 0:
                switch(j, i, self.table)
                i += 1
                j -= 1
        divideIndex = i
        return divideIndex


    def sort(self, beginningOfTable,endOfTable):
        if (endOfTable - beginningOfTable) <= 1:
            return 1
        randomValue = self.table[random.randint(beginningOfTable,endOfTable)]
        divideIndex = self.divide(beginningOfTable, endOfTable, randomValue)
        self.sort(beginningOfTable, divideIndex-1)
        self.sort(divideIndex, endOfTable)


    def randomTable(numberOfObjects, minValue, maxValue):
        table = []
        random.seed()  # initialize random generator, where current time is seed parameter
        for i in range(numberOfObjects):
            table.append(
                random.randint(minValue, maxValue))  # add into the table int number, where minValue<= number <=maxValue
        return table



y = QuickSort(1, 10000)
y.table = [90, 20, 3, 4, 7, 15, 10, 8]
y.sort(0, 7)
print (y.table)

x = QuickSort(1, 1000)
numberOfObjects = 1000
x.table = QuickSort.randomTable(numberOfObjects, x.minValue, x.maxValue)
x.sort(0,numberOfObjects-1)
print (x.table)