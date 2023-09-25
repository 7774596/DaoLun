num1,num2,num3 = input("请输入要比较的3个数字：").split()

numbers = [int(num1), int(num2), int(num3)]
print(numbers[0],numbers[1],numbers[2])
n = len(numbers)
for i in range(0,2):
    for j in range(0, 2 - i):
        if numbers[j] < numbers[j + 1]:
            # 交换两个数
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("排序后的结果为:", numbers)