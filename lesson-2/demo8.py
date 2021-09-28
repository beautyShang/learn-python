class Node():

    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode


def getNumber(input, index):
    if index == 0:
        return input.value
    return getNumber(input.nextNode, index - 1)


bigNode = Node(2, Node(5, Node(10, Node(2, None))))


def removeNode(index, node):
    if index == 0:
        return node.nextNode
    return Node(node.value, removeNode(index - 1, node.nextNode))


targetNode = removeNode(2, bigNode)
print(getNumber(targetNode, 0))
print(getNumber(targetNode, 1))
print(getNumber(targetNode, 2))
print(getNumber(targetNode, 3))
