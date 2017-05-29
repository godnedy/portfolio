class LNDS:  # LNDS - Longest NonDecreasing Subsequence

    subsequence = []
    sortedSubsequence = []
    subsequenceLength = 0

    table = []

    def __init__(self, subsequenceInt, sortedSubsequenceInt):
        self.subsequence = subsequenceInt
        self.sortedSubsequence = sortedSubsequenceInt
        self.subsequenceLength = len(subsequenceInt)
        self.initializeTable()

    # this function initializes table which will be used to calculate the longest Longest NonDecreasing Subsequence with help of dynamic programing
    def initializeTable(self):
        for i in range(self.subsequenceLength + 1):
            self.table.append([0] * (self.subsequenceLength + 1))
    # solves the task by analogy to the Longest Common string subsequence. Firs subsequence is original list of numbers, second is sorted list of numbers
    def solve(self):
        for i in range(1,self.subsequenceLength + 1):
            for j in range(1, self.subsequenceLength + 1):
                if self.subsequence[j-1] == self.sortedSubsequence[i-1]: #last letters the same
                    self.table[j][i] = self.table[j-1][i-1] + 1
                else:
                    self.table[j][i] = max(self.table[j-1][i], self.table[j][i-1])
        # print(self.table)
        print(self.table[self.subsequenceLength][self.subsequenceLength])

# this function reads string, converts it into list of ints, duplicates it and sorts ascending, and returns two lists: original and sorted
def readSubsequenceAndTransform():
    subsequence = input()
    subsequenceInt = [int(i) for i in subsequence.split(" ")]
    print(subsequenceInt)
    sortedSubsequenceInt = sorted(subsequenceInt, key = int)
    print(sortedSubsequenceInt)
    subsequences = []
    subsequences.append(subsequenceInt)
    subsequences.append(sortedSubsequenceInt)

    return subsequences

subseqences = readSubsequenceAndTransform()
lcs = LNDS(subseqences[0], subseqences[1])
lcs.solve()