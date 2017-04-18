class Sums:

    n = 0  # number for which max number of sums is calculated
    smartTable = []

    def __init__(self, n):
        self.n = n
        self.initializeTable()

    # initializes table where subsums are stored
    def initializeTable(self):
        self.smartTable = (self.n + 1) * [0]
        self.smartTable[0] = 1


    # n^2
    # w kolejnych przejsciach petli mamy do dyspozycji i = 1, 2 , 3 , 4 ,5, ..., n itp. Przechodzimy po tablicy od n w lewa strone (malejącą) i dla kazdego indeksu j od prawej dodajemy
    # to co w indeksie j-i. Na koniec odejmujemy 1 od wyniku (bo to co obliczyliśmy uwzględnia rowniez sumy jednoelementowe.
    def solveSmart(self):
        if self.n < 3:
            return 0
        else:
            for i in range(1, self.n + 1, 1):
                for j in range(self.n, i - 1, -1):
                    self.smartTable[j] += self.smartTable[j-i]
        print(self.smartTable)
        return self.smartTable[self.n] - 1



x = int(input())
s = Sums(x)
print(s.smartTable)
print(s.solveSmart())