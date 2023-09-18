n = int(input("请输入要求阶乘的数字:"))
s = 1
for i in range(1, n + 1):
    s *= i
    i += 1

print("结果是:", s)