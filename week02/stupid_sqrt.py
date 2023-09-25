


def stupid_sqrt(a):
    g = float(0)
    global i
    while abs(g*g - a) > 0.0001:
        g = g + 0.00001
        i += 1
        if abs(g * g - a) <= 0.0001:
            return float(g)


if __name__ == "__main__":
    i = 0
    a = int(input("请输入被开平方数值："))
    print(stupid_sqrt(a), "运算次数为：", i)