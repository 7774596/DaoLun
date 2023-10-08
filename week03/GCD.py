
def max_num(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2


def min_num(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2


def switch_division(num1, num2):
    tmp = max_num(num1, num2) % min_num(num1, num2)
    if tmp == 0:
        return min_num(num1, num2)
    else:
        num1 = min_num(num1, num2)
        num2 = tmp
        return switch_division(num1, num2)



if __name__ == "__main__":
    print("请输入两个整数：")
    a = int(input())
    b = int(input())
    print("这两个数的最大公因数是：", switch_division(a, b))
