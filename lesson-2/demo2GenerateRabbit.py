def generateRabbit(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return generateRabbit(n - 1) + generateRabbit(n - 2)
n = input("Please input n:")
print(generateRabbit(int(n)))
