def buyDuck(number, index):
    if (index == 0):
        return number
    number = (number + 1) * 2
    return buyDuck(number, index - 1)


index = input("请输入经过的村子的数量：")
print(buyDuck(2, int(index)))
