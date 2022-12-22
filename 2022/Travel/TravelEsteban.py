

class Structure():

    def __init__(self, nodes: int, startFuel: int, start_cost: int):
        self.nodes: int = nodes
        self.currentFuel: int = startFuel
        self.currentCost: int = start_cost
        self.listOfNodes: list = []
        self.listOfLinks: list = []

    def addNode(self, node: int, link: int):
        self.listOfNodes.append(node)
        self.listOfLinks.append(link)

    def goTo(self, dest: int):
        for i in range(dest):
            self.currentFuel -= self.listOfLinks[i]

        self.currentCost += self.listOfNodes[i]*self.listOfNodes[i] + 500
        self.listOfNodes = self.listOfNodes[dest:]
        self.listOfLinks = self.listOfLinks[dest:]

    def minCost(self) -> int:
        if (self.listOfNodes == []):
            return self.currentCost
        else:
            minScope: int = self.MinScope(
                self.currentFuel, len(self.listOfNodes))
            minCost: int = self.cheapest(minScope)
            self.goTo(minCost)
            self.listOfNodes = self.listOfNodes[1:]
            self.listOfLinks = self.listOfLinks[1:]
            return self.minCost()

    def cheapest(self, scope: int) -> int:
        return min(self.listOfNodes[:scope])

    def MinScope(self, gas: int, i: int):
        print(self.getScope(0, 0, i))
        if (self.getScope(0, 0, i) <= gas):
            return i
        else:
            return self.MinScope(gas, i-1)

    def getScope(self, num: int, a: int, b: int) -> int:
        if (a == b):
            return num
        else:
            return self.getScope(num+self.listOfLinks[a], a+1, b)

#!


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


# input_parser = parser()
# for i in range(get_number()):
#     input_parser = parser()
#     nodes = get_number()
#     fuel = get_number()
#     start_cost = get_number()
#     structure = Structure(nodes, fuel, start_cost*fuel)
#     for i in range(nodes):
#         structure.addNode(get_number(), get_number())
#     print(structure.minCost())
structure = Structure(3, 35, 230*35)
structure.addNode(15, 240)
structure.addNode(15, 225)
structure.addNode(24, 240)
print(structure.minCost())
