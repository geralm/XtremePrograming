

class graph():
    def __init__(self, nodes: int, edges: int):
        self.streets: list = []
        self.adjacencyList: list = []

        self.initStreets(nodes)
        self.initMatrix(edges)

    def getStreets(self) -> list:
        return self.streets

    def getAdyacency(self) -> list:
        return self.adjacencyList

    def initStreets(self, n: int):
        for i in range(n):
            self.streets.append(i+1)

    def getEdge(self, i, j):
        return self.adjacencyList[i][j]

    def setEdge(self, i, j, w):
        self.adjacencyList[i-1][j-1] = w

    def initMatrix(self, n):
        self.adjacencyList = [[0 for x in range(n)] for y in range(n)]


class dijstra():
    def __init__(self, graph: graph, start=0):
        self.graph = graph
        self.start: int = start
        self.n: int = len(self.graph.getStreets())

        self.initCostMatrix()
        self.last: list = []
        self.minimumList: list = [0 for j in range(self.n)]
        self.visited: list = []

    def solve(self) -> list:
        record: list = []
        for i in range(self.n):
            self.visited.append(False)
            self.minimumList[i] = self.costMatrix[self.start][i]
            self.last.append(self.start)
        self.visited[self.start] = True
        self.minimumList[self.start] = 0
        for i in range(1, self.n):
            node: int = self.getminimun()
            if (node in record):
                break
            else:
                record.append(node)
            self.visited[node] = True
            for j in range(1, self.n):
                if not self.visited[j]:
                    if ((self.minimumList[node] + self.costMatrix[node][j]) < self.minimumList[j]):
                        self.minimumList[j] = (
                            self.minimumList[node] + self.costMatrix[node][j])
                        self.last[j] = node
        return self.minimumList

    def getminimun(self) -> int:
        maxN: int = 9999999
        node: int = 1
        for i in range(1, self.n):
            if not self.visited[i] and (self.minimumList[i] <= maxN):
                maxN = self.minimumList[i]
                node = i
        return node

    def initCostMatrix(self) -> list:
        self.costMatrix: list = [
            [0 for i in range(self.n)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                cost: int = self.graph.getEdge(i, j)
                if cost == 0:
                    self.costMatrix[i][j] = 9999999
                else:
                    self.costMatrix[i][j] = cost

        return self.costMatrix


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


input_parser = parser()
T = get_number()
input_parser = parser()
N = get_number()
graphStruct: graph = graph(T, N)
for t in range(N):
    input_parser = parser()
    graphStruct.setEdge(get_number(), get_number(), get_number())

dij: dijstra = dijstra(graphStruct)
l: list = dij.solve()
for i in l:
    print(i)
