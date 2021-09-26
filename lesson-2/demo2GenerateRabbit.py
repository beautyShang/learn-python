def generateRabbit(args):
    if args == 1:
        return 1
    if args == 2:
        return 1
    return generateRabbit(args - 1) + generateRabbit(args - 2)
n = input("Please enter the number n :")
print(generateRabbit(int(n)))
