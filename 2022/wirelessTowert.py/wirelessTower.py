

class Node():
    def __init__(self, name: str, isUpgrated: int):
        self.name = name
        if (isUpgrated == 1):
            self.isUpgrated = True
        else:
            self.isUpgrated = False


class Graph():

    def __init__(self, ):
        self.nodes: list = []
        self.edges: list = [[]]

    def addNode(self, str)
