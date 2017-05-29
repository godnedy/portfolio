import sys


class Coins:
    k = 0
    n = 0
    coins = []
    lastTable = [[0, -1]]  #where first value is the minimum number of coins needed, second is coin nominal which makes possible returning this value of odd money
    currentTable = [[0, -1]]


    #test data are as follows: line1 - k - sum of money n, line 2 - value of n coins with' ' between them
    #this method reads data from file and saves them
    @staticmethod
    def readData():
        file_name = input();
        fp = open(file_name)
        line = str(fp.readline()).split()
        Coins.k = int(line[0])
        Coins.n = int(line[1])
        line = fp.readline().split()
        for i in range (Coins.n):
            Coins.coins.append(int(line[i]))
        print(Coins.coins)

    @staticmethod
    def initializeTables():
        for i in range(Coins.k):
            Coins.lastTable.append([-1,-1])
            Coins.currentTable.append([-1, -1])

    def updateWithCoin(coin):
        for i in range (1,Coins.k+1):
            diff = i - coin
            if diff == 0:
                Coins.currentTable[i][0] = 1
                Coins.currentTable[i][1] = coin
            if diff > 0:
                if int(Coins.lastTable[diff][0]) > 0:
                    if Coins.currentTable[i][0] == -1 or Coins.lastTable[diff][0] + 1 < Coins.currentTable[i][0]:
                        Coins.currentTable[i][0] = Coins.lastTable[diff][0] + 1
                        Coins.currentTable[i][1] = coin
        Coins.copyTables(Coins.lastTable, Coins.currentTable)

    @staticmethod
    def solve():
        for coin in Coins.coins:
            Coins.updateWithCoin(coin)

    def copyTables (lastTable, currentTable):
        #print('last table: ')
        #print(lastTable)
        for i in range(Coins.k+1):
            lastTable[i] = currentTable[i][:]
        #print('current table: ')
        #print(currentTable)

    @staticmethod
    def printUsedCoins(amount):
        if Coins.currentTable[amount][0] > 0:
            usedCoins = []
            amountLeft = amount
            while amountLeft > 0:
                coin = Coins.currentTable[amountLeft][1]
                usedCoins.append(coin)
                amountLeft -= coin
            for coin in usedCoins:
                print(coin)
        else:
            print('Not possible for this amount')

Coins.readData()
Coins.initializeTables()
Coins.solve()
print("Coins used to return " + str(Coins.k) + " are as follows")
Coins.printUsedCoins(int(Coins.k))

