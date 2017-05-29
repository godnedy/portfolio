

class LCS:  # LCS - Longest Common Subsequence

    firstString = ""
    secondString = ""
    firstLength = 0
    secondLength = 0

    table = []

    def __init__(self, firstString, secondString):
        self.firstString = firstString
        self.secondString = secondString
        self.firstLength = len(self.firstString)
        self.secondLength = len(self.secondString)
        self.initializeTable()

    def initializeTable(self):
        for i in range(self.firstLength + 1):
            self.table.append([0] * (self.secondLength + 1))

    def solve(self):

        for i in range(1,self.secondLength + 1):
            for j in range(1, self.firstLength + 1):
                if self.firstString[j-1] == self.secondString[i-1]: #last letters the same
                    self.table[j][i] = self.table[j-1][i-1] + 1
                else:
                    self.table[j][i] = max(self.table[j-1][i], self.table[j][i-1])
        print(self.table)
        print(self.table[self.firstLength][self.secondLength])


def readData():
    # file_name = input();
    # fp = open(file_name)
    firstString = input()
    secondString = input()
    return [firstString, secondString]

strings = readData()
lcs = LCS(strings[0], strings[1])
lcs.solve()