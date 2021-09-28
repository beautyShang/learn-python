# 高斯求和

def caculateTotal(total, number):
    if number == 0:
        return total
    total = number + total
    return caculateTotal(total, number - 1)


input = input()
print(caculateTotal(0, int(input)))
