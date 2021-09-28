class Tree():

    def __init__(self, value, nextLeftTree, nextRightTree):
        self.value = value
        self.nextLeftTree = nextLeftTree
        self.nextRightTree = nextRightTree

    def getLeftNext(self):
        return self.nextLeftTree

    def getRightNext(self):
        return self.nextRightTree


def getMax(a, b):
    if a >= b:
        return a
    return b


def getDeepth(deepth, tree):
    if tree is None:
        return 0
    return getMax(getDeepth(deepth + 1, tree.nextLeftTree), getDeepth(deepth + 1, tree.nextRightTree)) + 1


targetTree = Tree(1, Tree(5, Tree(4, Tree(6, Tree(8, None, Tree(20, None, Tree(1, None, None))), Tree(10, None, None)),
                                  Tree(10, None, None)), Tree(10, None, None)), Tree(251, None, None))
print(getDeepth(0, targetTree))
