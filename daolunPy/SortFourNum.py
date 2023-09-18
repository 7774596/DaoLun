
num1,num2,num3,num4 = input("请输入要比较的4个数字：").split()

numbers = [int(num1), int(num2), int(num3), int(num4)]

n = len(numbers)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if numbers[j] < numbers[j + 1]:
            # 交换两个数
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("排序后的结果为:", numbers)
