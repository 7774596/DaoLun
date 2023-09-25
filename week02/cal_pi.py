import random
import math
def throwNeedles(numNeedles):# 蒙特卡洛方法扔针
    count = 0
    for i in range(numNeedles):
        x = random.random()
        y = random.random()
        if (x*x + y*y) <= 1:
            count += 1
    return 4 * (count/numNeedles)

result = []
def cal_everage(sum,numNeedles):# 计算某个精度下的平均数
    global result
    aver = 0
    sDev = 0
    for i in range(sum):
        pi = throwNeedles(numNeedles)
        result.append(pi)
    for i in range(sum):
        aver += result[i] / sum
    for i in range(sum):
        sDev += pow((result[i] - sDev), 2) / sum
    if sDev >= 2.387:
        print(sDev, sum)
        result.clear()
        cal_everage(sum + 10, numNeedles + 2000)

    return aver

#  定积分求四分之一象限的面积


def integral(n):
    mid = 0
    result = 0
    for i in range(n):
        mid = (i+0.5)/n
        result += 1/n * math.sqrt(1 - pow(mid, 2))
    result = 4*result
    return result


def sign(n):
    if n % 4 == 1:
        return 1
    else:
        return -1


# arctan(x)展开   pi/4 = ……


def arctan_pi(n):
    pi = 0
    sum = 0
    for i in range(1, n + 1):
        sum += (4 / (sign(2 * i - 1) * (2 * i - 1)))
    pi = sum
    return pi


if __name__ == "__main__":
    print(cal_everage(10, 40000))
    print(integral(1000))
    print(arctan_pi(100000))