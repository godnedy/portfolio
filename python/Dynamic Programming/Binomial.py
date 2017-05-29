import sys


class Binomial:

    def __init__(self, n, k):
        self.k = k
        self.n = n
        self.T = []
        for i in range (n+1):
            self.T.append([0]*(k+1))
        for i in range(n+1):
            self.T[i][0] = 1
        for i in range(k+1):
            self.T[i][i] = 1

    @staticmethod
    def readData(): #do dopisania
        line = str(sys.stdin.readline())
        n = line[0]
        k = line[1]
        if k>n:
            print('Wrong data')
            quit()
        else:
            print(line[0])
            print(line[1])

    def binomial(self):
        for i in range(1,self.k + 1):
            for j in range (i+1,self.n + 1):
                self.T[j][i] = self.T[j-1][i-1] + self.T[j-1][i]
        print (self.T[self.n][self.k])
        return (self.T[self.n][self.k])



#Binomial.readData()
b = Binomial(6,4)
b.binomial()
