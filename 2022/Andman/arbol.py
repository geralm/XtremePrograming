

class Node:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, id, weight):
        if self.root is None:
            self.root = Node(id[0], weight)
        else:
            self._add(id, weight, self.root)

    def _add(self, id, weight, node):
        if node is None:
            pass
        elif node.left is None:
            if node.id == id[0]:
                node.left = Node(id[1], weight)
            else:
                self._add(id, weight, node.left)
        elif node.right is None:
            if node.id == id[0]:
                node.right = Node(id[1], weight)
            else:
                self._add(id, weight, node.right)
        else:
            self._add(id, weight, node.left)
            self._add(id, weight, node.right)

    def isLeaf(self, node):
        if node.left is None and node.right is None:
            return True
        else:
            return False

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            print(node.id, node.weight)
            self._printTree(node.left)
            self._printTree(node.right)

    def find_least_common_ancestor(self, nodo: Node, n1: int, n2: int) -> Node:
        # Base case
        if nodo is None:
            return nodo
        # If either n1 or n2 matches with root's
        # key, report the presence by returning root
        if nodo.id == n1 or nodo.id == n2:
            return nodo
        # Look for keys in left and right subtrees
        left = self.find_least_common_ancestor(nodo.left, n1, n2)
        right = self.find_least_common_ancestor(nodo.right, n1, n2)

        if left and right:
            return nodo

        # Otherwise check if left subtree or
        # right subtree is Least Common Ancestor
        if left:
            return left
        else:
            return right

    # sum of weights of all nodes on the path from root to n, where n is a given node in the tree

    def calculateSum(self, temp):
        sum = sumRight = sumLeft = 0

        # Check whether tree is empty
        if (self.root == None):
            print("Tree is empty")
            return 0
        else:
            # Calculate the sum of nodes present in left subtree
            if (temp.left != None):
                sumLeft = self.calculateSum(temp.left)

            # Calculate the sum of nodes present in right subtree
            if (temp.right != None):
                sumRight = self.calculateSum(temp.right)

            # Calculate the sum of all nodes by adding sumLeft, sumRight and root node's data
            sum = temp.weight + sumLeft + sumRight
        return sum

    def calculateWeight1(self, node, id1):
        weight = 1
        if node is not None:
            weight *= node.weight
            weight *= self.calculateWeight1(node.left, id1)
            #weight *= self.calculateWeight(node.right, id1)
        return weight

    def calculateWeight2(self, node, id1):
        weight = 1
        if node is not None:
            weight *= node.weight
            #weight *= self.calculateWeight(node.left, id1)
            weight *= self.calculateWeight2(node.right, id1)
        return weight


def findFather(nodes: list):
    for i in range(len(nodes)):
        isFather = True
        for j in range(len(nodes)):
            if i != j:
                if nodes[i][0] == nodes[j][1]:
                    isFather = False
        if isFather:
            return i


# print(findFather([[3,1],[2,5],[3,6],[4,3],[4,2]]))

def orderList(nodes: list):
    father = findFather(nodes)
    orderedList = []
    orderedList.append(nodes.pop(father))
    actInd = [orderedList[-1][0], orderedList[-1][1]]
    while 0 < len(nodes):
        j = 0
        while j < len(nodes):
            if nodes[j][0] == actInd[0]:
                orderedList.append(nodes.pop(j))
                actInd += [orderedList[-1][1]]
            j += 1
            if (j == 1 and j == len(nodes)):
                j -= 1
        actInd.pop(0)
    return orderedList


#listaOrd = orderList([[1,2],[1,3],[2,4],[2,5]])
#listaWeight = [9, 11, 11, 13, 13]
listaOrd = orderList([[3, 1], [2, 5], [3, 6], [4, 3], [4, 2]])
listaWeight = [500000, 6, 5, 7, 300000, 400000]
print(listaOrd)
nodosCreados = []


tree = Tree()
for i in range(len(listaOrd)):
    if listaOrd[i][0] not in nodosCreados:
        tree.add(listaOrd[i], listaWeight[0])
        nodosCreados.append(listaOrd[i][0])
        listaWeight.pop(0)
    if listaOrd[i][1] not in nodosCreados:
        tree.add(listaOrd[i], listaWeight[0])
        nodosCreados.append(listaOrd[i][1])
        listaWeight.pop(0)

print(tree.find_least_common_ancestor(tree.root, 4, 5))
print(tree.calculateWeight1(tree.find_least_common_ancestor(tree.root, 1, 6), 1))
print(tree.calculateWeight2(tree.find_least_common_ancestor(tree.root, 1, 6), 6))

tree.printTree()
print("")


def findNode(self, node, id1, weight):
    if node is not None:
        if node.id == id1:
            node.weight = weight
            print(node.weight)
        else:
            self.findNode(node.left, id1, weight)
            self.findNode(node.right, id1, weight)
