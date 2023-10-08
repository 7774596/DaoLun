
def cal(i, array):
    sum = 1
    for j in range(i):
        sum *= int(array[j])
    for j in range(i+1, len(array)):
        sum *= int(array[j])
    return sum


if __name__ == "__main__":
    print("请输入初始数组：")
    a = input().split()
    b = []
    for i in range(len(a)):
        b.append(int(cal(i, a)))
    print("修改过的数组为：", b)