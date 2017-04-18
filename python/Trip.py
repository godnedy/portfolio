class Trip:
    def __init__(self):
        self.connections = {}  # dictionary with cities and their connections
        self.numberOfConnections = 0

    #private functions
    def __addConnection(self, departureDestination, arrivalDestination):
        if departureDestination in self.connections:
            self.connections[departureDestination].append(arrivalDestination)
        else:
            self.connections[departureDestination] = [arrivalDestination]
        return 1


    def __findRouteBeginning(self):
        for key in self.connections:
            if len(self.connections[key])== 1:
                return key
        else:
            print('Wrong file provided')
            quit()

    #publicFunctions
    def readConnectionsFromFile(self, path):
        try:
            file = open(path)
        except IOError:
            print('File not found')
            quit()   # end of program
        else:
            self.numberOfConnections = int(file.readline())
            iterator = self.numberOfConnections
            while (iterator > 0):
                line = file.readline()
                dashindex = line.find("-")
                if dashindex >=0:
                    city1 = line[0:dashindex]
                    city2 = line[dashindex+1:len(line)-1]
                    self.__addConnection(city1, city2)
                    self.__addConnection(city2, city1)
                    iterator -= 1
                else:
                    print('Connections not properly written')
                    quit()

    def printRoute(self):     # prints route for particular trip
        route = ""
        routeBeginning = self.__findRouteBeginning()
        route += routeBeginning
        key = self.connections[routeBeginning][0]
        route += "-"
        route += key
        previousKey = routeBeginning
        iterator = self.numberOfConnections - 1
        while (iterator > 0):
            route += "-"
            value = self.connections[key]
            print (value)
            if value[0] == previousKey:
                route += value[1]
                previousKey = key
                key = value[1]
            else:
                route += value[0]
                previousKey = key
                key = value[0]
            iterator -= 1
        print(route)

    def printConnections(self):
        print(self.connections)

#TESTING
x = Trip()
y = Trip()
z = Trip()

x.readConnectionsFromFile("C:\\DaneEdyta\\akademiadzie2\\dane1.txt")
x.printConnections()
x.printRoute()


y.readConnectionsFromFile("C:\\DaneEdyta\\akademiadzie2\\dane2modified.txt")
y.printConnections()
y.printRoute()

z.readConnectionsFromFile("C:\\DaneEdyta\\akademiadzie2\\dane3.txt")
z.printConnections()
z.printRoute()





