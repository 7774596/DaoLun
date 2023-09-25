import random
import math

def cal_integral(n):
    count = 0
    for i in range(n):
        x = random.uniform(2.0, 3.0)
        y = random.uniform(0.0, 13.0)
        # print(x, pow(x, 2) + 4*x*math.sin(x), y)
        if(y <= pow(x, 2) + 4*x*math.sin(x)):
                count += 1
    result = 13 * count/n
    print(count)
    return result

print(cal_integral(200000))


