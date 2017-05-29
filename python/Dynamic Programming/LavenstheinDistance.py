class Lavensthein:
    originalString = ""
    toBeString = ""
    originalLength = 0
    toBeLength = 0

    table = []

    def __init__(self, originalString, toBeString):
        self.originalString = originalString
        self.toBeString = toBeString
        self.originalLength = len(self.originalString)
        self.toBeLength = len(self.toBeString)
        self.initializeTable()

    def initializeTable(self):
        for i in range(self.originalLength + 1):
            self.table.append([0] * (self.toBeLength + 1))
            self.table[i][0] = i
        for i in range(self.toBeLength+1):
            self.table[0][i] = i
        #print(self.table)

    def solve(self):
        for i in range(1,self.toBeLength + 1):
            for j in range(1, self.originalLength + 1):
                if self.originalString[j-1] == self.toBeString[i-1]: #last letters the same
                    self.table[j][i] = self.table[j-1][i-1]
                else:
                    add = 1 + self.table[j][i-1]
                    switch = 1 + self.table[j-1][i-1]
                    delete = 1 + self.table[j-1][i]
                    self.table[j][i] = min(add, switch, delete)
        #print(self.table)
        print(self.table[self.originalLength][self.toBeLength])



# returns list with original and toBe string
def readData():
    # file_name = input();
    # fp = open(file_name)
    originalString = input()
    toBeString = input()
    return [originalString, toBeString]



line = readData()
ld = Lavensthein(line[0], line[1])
ld.solve()
