class Node():

    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode


def addNode(index, node, number):
    if index == 0:
        return Node(number, node)
    return Node(node.value, addNode(index - 1, node.nextNode, number))


def getNumber(input, index):
    if index == 0:
        return input.value
    return getNumber(input.nextNode, index - 1)


bigNode = Node(2, Node(5, Node(10, Node(2, None))))
targetNode = addNode(2, bigNode, 15)
print(getNumber(targetNode, 0))
print(getNumber(targetNode, 1))
print(getNumber(targetNode, 2))
print(getNumber(targetNode, 3))
print(getNumber(targetNode, 4))
