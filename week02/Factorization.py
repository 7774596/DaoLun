n = int(input("请输入要分解的正整数："))

s = int(n)
def cal_int(x):
    result = 0
    if x < 4:
        result = x - 1
    if x == 4:
        result = 4
    if x >= 5:
        factor = int(x/3)
        res = int(x % 3)
        if res == 1:
            factor -= 1
            res = 4
        if res != 0:
            result = pow(3, factor) * res
        else:
            result = pow(3, factor)
    return result

print("拆分后乘积为：", cal_int(s))