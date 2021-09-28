# n! = n * (n - 1) * (n - 2) * ... * 1

def getNumber(total, number):
    if number == 0:
        return total
    total = total * number
    return getNumber(total, number - 1)


input = input()
print(getNumber(1, int(input)))
 