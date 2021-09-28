# 角谷定理。输入一个自然数，若为偶数，则把它除以2，
# 若为奇数，则把它乘以3加1。经过如此有限次运算后，总可以得到自然数值1。求经过多少次可得到自然数1

# 如：输入22，
#
# 输出 STEP=16

def caculateStep(step, number):
    if number == 1:
        return step + 1
    if number % 2 == 0:
        number = number / 2
    else:
        number = number * 3 + 1
    return caculateStep(step + 1, number)


input = input()
print(caculateStep(0, int(input)))
