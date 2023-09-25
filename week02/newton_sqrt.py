

def newton_sqrt(a):
    g = float(a/2)
    i = 0
    while abs(g*g - a) > 1e-8:
        g = (g + a/g)/2
        i += 1
    print("结果是：", g, "运算次数是：", i)




if __name__ == "__main__":
    a = int(input("请输入开平方的数字："))
    newton_sqrt(a)