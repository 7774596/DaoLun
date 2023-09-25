def newton_cubic(a):
    g = float(a/2)
    i = 0
    while abs(g*g*g - a) > 1e-8:
        g = 2*g/3 + a/(3*g*g)
        i += 1
    print("结果是：", g, "运算次数是：", i)




if __name__ == "__main__":
    a = int(input("请输入开立方的数字："))
    newton_cubic(a)