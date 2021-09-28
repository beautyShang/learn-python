class Box():

    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode


def getNumber(input, index):
    if index == 0:
        return input.value
    return getNumber(input.nextNode, index - 1)


input = Box('Green', Box('Red', Box('Yellow', None)))
# I want to print the third number of input:
print(getNumber(input, 2))
